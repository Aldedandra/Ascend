const PRONUNCIATIONS = [
  [/\bCI\/CD\b/g, "continuous integration and continuous delivery"],
  [/\bAPI\b/g, "A P I"],
  [/\bAPIs\b/g, "A P I's"],
  [/\bDNS\b/g, "D N S"],
  [/\bHTTP\b/g, "H T T P"],
  [/\bHTTPS\b/g, "H T T P S"],
  [/\bIP\b/g, "I P"],
  [/\bIPs\b/g, "I P addresses"],
  [/\bCPU\b/g, "C P U"],
  [/\bRAM\b/g, "ram"],
  [/\bURL\b/g, "U R L"],
  [/\bURLs\b/g, "U R L's"],
  [/\bUI\b/g, "U I"],
  [/\bUX\b/g, "U X"],
  [/\bCLI\b/g, "C L I"],
  [/\bJSON\b/g, "jay son"],
  [/\bYAML\b/g, "yam ul"],
  [/\bSQL\b/g, "sequel"],
  [/\bSSH\b/g, "S S H"],
  [/\bTLS\b/g, "T L S"],
  [/\bTCP\b/g, "T C P"],
  [/\bUDP\b/g, "U D P"],
  [/\bAWS\b/g, "A W S"],
  [/\bIAM\b/g, "I A M"],
  [/\bVPC\b/g, "V P C"],
  [/\bEC2\b/g, "E C two"],
  [/\bS3\b/g, "S three"],
];

function appendMapped(output, map, text, sourceIndex) {
  output.push(text);
  for (let index = 0; index < text.length; index += 1) {
    map.push(sourceIndex);
  }
}

function appendSource(output, map, text, sourceStart) {
  output.push(text);
  for (let index = 0; index < text.length; index += 1) {
    map.push(sourceStart + index);
  }
}

function replaceWithMapping(text, sourceMap, pattern, replacement) {
  const output = [];
  const map = [];
  let cursor = 0;

  text.replace(pattern, (match, ...args) => {
    const offset = args.at(-2);
    appendSource(output, map, text.slice(cursor, offset), cursor);
    appendMapped(output, map, replacement, sourceMap[offset] ?? offset);
    cursor = offset + match.length;
    return match;
  });

  appendSource(output, map, text.slice(cursor), cursor);
  return { text: output.join(""), map };
}

function applyPronunciations(text, map) {
  let currentText = text;
  let currentMap = map;

  for (const [pattern, replacement] of PRONUNCIATIONS) {
    const output = [];
    const outputMap = [];
    let cursor = 0;

    currentText.replace(pattern, (match, ...args) => {
      const offset = args.at(-2);
      output.push(currentText.slice(cursor, offset));
      outputMap.push(...currentMap.slice(cursor, offset));
      appendMapped(output, outputMap, replacement, currentMap[offset] ?? 0);
      cursor = offset + match.length;
      return match;
    });

    output.push(currentText.slice(cursor));
    outputMap.push(...currentMap.slice(cursor));
    currentText = output.join("");
    currentMap = outputMap;
  }

  return { text: currentText, map: currentMap };
}

function normalizeLine(line) {
  return line
    .replace(/^\s*[-*•]\s+/, "")
    .replace(/^\s*\d+[.)]\s+/, "")
    .trim();
}

function looksLikeHeading(line) {
  const normalized = normalizeLine(line);
  if (!normalized || normalized.length > 72) return false;
  if (/[.!?]$/.test(normalized)) return false;
  const words = normalized.split(/\s+/);
  return words.length <= 9;
}

/**
 * Convert a lesson script into speech-friendly text while retaining a mapping
 * back to the original source indexes used by Ascend's saved progress.
 */
export function formatForNarration(sourceText) {
  const source = String(sourceText || "").replace(/\r\n?/g, "\n");
  const output = [];
  const map = [];
  const lines = source.split("\n");
  let sourceCursor = 0;
  let listIndex = 0;

  lines.forEach((rawLine, lineIndex) => {
    const lineStart = sourceCursor;
    sourceCursor += rawLine.length + (lineIndex < lines.length - 1 ? 1 : 0);
    const trimmed = rawLine.trim();

    if (!trimmed) {
      if (output.length && !output.at(-1).endsWith("\n\n")) {
        appendMapped(output, map, "\n\n", Math.max(0, lineStart - 1));
      }
      listIndex = 0;
      return;
    }

    const bulletMatch = rawLine.match(/^\s*[-*•]\s+(.*)$/);
    const numberedMatch = rawLine.match(/^\s*(\d+)[.)]\s+(.*)$/);

    if (bulletMatch || numberedMatch) {
      const itemText = normalizeLine(rawLine);
      const ordinal = listIndex === 0
        ? "First"
        : listIndex === 1
          ? "Next"
          : "Then";
      appendMapped(output, map, `${ordinal}. `, lineStart);
      appendSource(output, map, itemText, lineStart + rawLine.indexOf(itemText));
      if (!/[.!?]$/.test(itemText)) {
        appendMapped(output, map, ".", lineStart + rawLine.length - 1);
      }
      appendMapped(output, map, "\n\n", lineStart + rawLine.length - 1);
      listIndex += 1;
      return;
    }

    listIndex = 0;

    if (looksLikeHeading(rawLine)) {
      appendMapped(output, map, "New section.\n\n", lineStart);
      appendSource(output, map, trimmed, lineStart + rawLine.indexOf(trimmed));
      appendMapped(output, map, ".\n\n", lineStart + rawLine.length - 1);
      return;
    }

    appendSource(output, map, trimmed, lineStart + rawLine.indexOf(trimmed));
    if (!/[.!?…]$/.test(trimmed)) {
      appendMapped(output, map, ".", lineStart + rawLine.length - 1);
    }
    appendMapped(output, map, "\n\n", lineStart + rawLine.length - 1);
  });

  let narrationText = output.join("")
    .replace(/\n{3,}/g, "\n\n")
    .trim();
  let narrationMap = map.slice(0, narrationText.length);

  const pronounced = applyPronunciations(narrationText, narrationMap);
  narrationText = pronounced.text;
  narrationMap = pronounced.map;

  return {
    text: narrationText,
    sourceIndexForNarrationIndex(index) {
      if (!narrationMap.length) return 0;
      const safeIndex = Math.max(0, Math.min(Number(index) || 0, narrationMap.length - 1));
      return narrationMap[safeIndex] ?? 0;
    },
  };
}
