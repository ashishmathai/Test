# Test

echo "# Test" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M master
git remote add origin git@github.com:ashishmathai/Test.git
git push -u origin master
