$dir=Join-Path (Get-Location) 'subjects\Nguyên lý kế toán\solutions'
Get-ChildItem -LiteralPath $dir -Filter '*_solution.md'|ForEach-Object{
 $chapter=[int]([regex]::Match($_.Name,'chuong-(\d+)').Groups[1].Value);$lines=Get-Content -Encoding UTF8 $_.FullName;$q=0
 for($i=0;$i -lt $lines.Count;$i++){
  if($lines[$i] -match '^## Câu (\d+)$'){$q=[int]$Matches[1];continue}
  if($lines[$i] -match '^\*\*Đề:\*\*\s+(.+)$'){
   $words=$Matches[1] -split '\s+';if($words.Count -gt 6){$lines[$i]='**Đề:** '+(($words[0..4]-join ' ')+' <!-- C'+$chapter+'.'+$q+'.DE --> '+($words[5..($words.Count-1)]-join ' '))}
  }elseif($lines[$i] -match '^- \*\*([A-D])\.\*\*\s*(.*?)\s+- \*\*(Đúng|Sai)\.\*\*(.*)$'){
   $letter=$Matches[1];$option=$Matches[2];$verdict=$Matches[3];$tail=$Matches[4];$words=$option -split '\s+'
   if($words.Count -gt 6){$option=(($words[0..4]-join ' ')+' <!-- C'+$chapter+'.'+$q+'.'+$letter+' --> '+($words[5..($words.Count-1)]-join ' '))}
   $lines[$i]="- **$letter.** $option - **$verdict.**$tail"
  }
 }
 [System.IO.File]::WriteAllText($_.FullName,($lines -join "`r`n")+"`r`n",[System.Text.UTF8Encoding]::new($false));Write-Host $_.Name
}
