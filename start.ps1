Write-Host "Building and starting The Journey Hub..." -ForegroundColor Cyan
docker compose up -d --build

Write-Host ""
Write-Host "The Journey Hub should now be available at:" -ForegroundColor Green
Write-Host "  http://localhost:3001"
Write-Host ""
Write-Host "To access it from another device, use your Windows computer's local IP:" -ForegroundColor Yellow
Write-Host "  http://YOUR-PC-IP:3001"
Write-Host ""
Write-Host "View logs with: docker compose logs -f"
