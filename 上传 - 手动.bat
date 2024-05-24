chcp 65001
git status
git add .
git commit -m "first commit"
git pull
# 检查是否有冲突
if [ $? -eq 0 ]; then
  # 没有冲突，执行推送
  git push -u origin aiiw
pause
else
  # 有冲突，提醒用户解决冲突后手动推送
  echo "有合并冲突，请手动解决后执行 git push"
pause
fi
pause