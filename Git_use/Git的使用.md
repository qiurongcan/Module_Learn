Mac查看隐藏的文件 <font style="color:rgb(17, 17, 17);">CMD + Shift +.</font>

<font style="color:rgb(17, 17, 17);">Linux ：Ctrl + H</font>

仓库名称由两部分组成：用户名和仓库名

 

<h2 id="OhK0g">1.与git仓库建立连接</h2>
```python
# 用户名
git config --global user.name "注册名"
# 邮箱
git config --global user.email "注册邮箱"

# 如果电脑之前没有和github建立联系的话，则需要进行这一步的操作

# 生成ssh
ssh-keygen -t rsa -C "自己的邮箱"

```

<h3 id="fzjfM">1.1 第一次上传公钥</h3>
```python
# 生成ssh。github账号的邮箱
ssh-keygen -t rsa -C "自己的邮箱"
```

![图片中可以看到公钥的位置](https://cdn.nlark.com/yuque/0/2024/png/38974844/1717211649441-ad7f5cb1-b5bc-4dd8-a81b-f6cd9fe0a470.png)



<h3 id="ykNSv">2.2打开公钥的位置</h3>
![](https://cdn.nlark.com/yuque/0/2024/png/38974844/1717211929423-4f67c84d-db82-4c13-8028-d3e200f57d1d.png)

复制全文，公钥信息

```python
# 公钥的字符串
```



<h3 id="hvWTN">1.3打开Github，在Settings中点击SSH</h3>
![](https://cdn.nlark.com/yuque/0/2024/png/38974844/1717212430558-4b114571-e625-483f-a481-c66eeaf5f8a2.png)

<h3 id="tPLlf">1.4新建后添加公钥后保存</h3>
![](https://cdn.nlark.com/yuque/0/2024/png/38974844/1717212572002-7759481e-db5b-4408-b8d4-bf0b03f3e76c.png)

至此成功建立连接



<h3 id="Dm14A">1.5测试是否成功</h3>
```python
ssh -T git@github.com
```

此处要输入yes，否则会报错

![](https://cdn.nlark.com/yuque/0/2024/png/38974844/1717212678015-cf8bcf04-941e-44d1-a330-b6fff1c5d1df.png)



<h2 id="ad1zq">2.添加文件并进行提交</h2>
<h3 id="VHkAg">2.1修改文件内容</h3>
```python
echo "# My First Repository" >> README.md
```

<h3 id="rvTYL">2.2查看修改的文件状态</h3>
```python
# 查看文件的状态
git status
# 保存文件到暂存区
git add README.md
git add . # 添加所有文件
```

****

<h3 id="lYt1z">2.3提交更改</h3>
```python
git commit -m "Initial commit"
```

**以上的操作都是在本地的，还没有push到github上！！！**

<h2 id="sYpwP">3.将代码推送至github上</h2>
<h3 id="k83dJ">3.1在github上建立一个仓库</h3>
复制仓库的git链接，建立链接

```python
git remote add origin https://github.com/username/my-first-repo.git
```

或者可以直接git clone

```python
git remote add origin https://github.com/username/my-first-repo.git
```



<h3 id="tBF3X">3.2将本地提交推送至github上</h3>
```python
# 如果是master则选用master
git push -u origin master 
# 如果是main则选用main
git push -u origin main
```

<h3 id="GlAX9">3.3 如果push失败，则可以使用代理</h3>
```cpp
# 设置 HTTP 代理
git config --global http.proxy http://127.0.0.1:7890

# 设置 HTTPS 代理
git config --global https.proxy https://127.0.0.1:7890

# 如果要取消代理设置
git config --global --unset http.proxy
git config --global --unset https.proxy
```



<h2 id="t6rKK">4.创建分支，提交代码</h2>
<h3 id="g5nRT">4.1这个也是在本地操作，分支也可以上传至github</h3>
```python
# 查看分支
git branch

# 创建新的分支
git branch <new-branch-name>

# 切换分支
git checkout myBranch

# 创建并切换分支
git checkout -b myBranch

```

<h3 id="ZrmSs">4.2上传分支</h3>
```python
# 拉取分支
git pull origin <branch>
# 添加修改
git add .
# 保存
git commit -m "change branch"

git push origin <branch>
```



<h3 id="As3IG">4.3完整的操作</h3>
```python
# 1. 先获取远程更新
git fetch origin

# 2. 查看状态
git status

# 3. 拉取并合并远程更改
git pull origin logger

# 4. 如果有冲突，解决冲突
# 编辑冲突文件

# 5. 添加更改
git add .

# 6. 提交更改
git commit -m "merge remote changes"

# 7. 推送到远程
git push origin logger
```



<h2 id="RLkDc"><font style="color:rgb(55, 65, 81);">5在 Git 中为 GitHub 上的分支打标签（tag）</font></h2>
<font style="color:rgb(55, 65, 81);">是一个常见的操作，通常用于标记特定的版本或重要的提交。以下是如何在本地创建标签并将其推送到 GitHub 的步骤。</font>

<h3 id="71c14ae2">步骤 1：查看现有标签</h3>
<font style="color:rgb(55, 65, 81);">在开始之前，可以查看当前仓库中已有的标签：</font>

```plain
bash复制代码
git tag
```

<h3 id="8f1ebcb2">步骤 2：创建新标签</h3>
1. **创建轻量标签**<font style="color:rgb(55, 65, 81);">： 如果您只想标记某个提交（例如，当前的 HEAD），可以创建一个轻量标签：</font>

```plain
bash复制代码
git tag <tag-name>
```

<font style="color:rgb(55, 65, 81);">示例：</font>

```plain
bash复制代码
git tag v1.0
```

2. **创建附注标签**<font style="color:rgb(55, 65, 81);">： 附注标签可以包含更多信息，例如作者、日期和标签说明:</font>

```plain
bash复制代码
git tag -a <tag-name> -m "Your message"
```

<font style="color:rgb(55, 65, 81);">示例：</font>

```plain
bash复制代码
git tag -a v1.0 -m "Release version 1.0"
```

<h3 id="272b271a">步骤 3：查看标签信息</h3>
<font style="color:rgb(55, 65, 81);">您可以查看标签的详细信息：</font>

```plain
bash复制代码
git show <tag-name>
```

<font style="color:rgb(55, 65, 81);">示例：</font>

```plain
bash复制代码
git show v1.0
```

<h3 id="13594cf0">步骤 4：推送标签到 GitHub</h3>
<font style="color:rgb(55, 65, 81);">要将本地标签推送到远程 GitHub 仓库，使用以下命令：</font>

```plain
bash复制代码
git push origin <tag-name>
```

<font style="color:rgb(55, 65, 81);">示例：</font>

```plain
bash复制代码
git push origin v1.0
```

<h3 id="ad95c40b">步骤 5：推送所有标签（可选）</h3>
<font style="color:rgb(55, 65, 81);">如果您想一次性将所有标签推送到远程仓库，可以使用以下命令：</font>

```plain
bash复制代码
git push --tags
```

<h3 id="5be534e9">步骤 6：在 GitHub 上查看标签</h3>
<font style="color:rgb(55, 65, 81);">完成以上步骤后，您可以导航到您的 GitHub 仓库，点击“Releases”或“Tags”标签查看刚刚推送的标签。</font>

<font style="color:rgb(55, 65, 81);"></font>

<h2 id="SaXmh"><font style="color:rgb(55, 65, 81);">6在 GitHub 上删除分支</font></h2>
<font style="color:rgb(55, 65, 81);">是一个相对简单的操作，可以通过 GitHub 网站界面或者 Git 命令行来完成。以下是两种方法的详细步骤：</font>

<h3 id="47049bf6">方法 1：通过 GitHub 网站删除分支</h3>
1. **登录到 GitHub**<font style="color:rgb(55, 65, 81);">： 打开浏览器，访问 </font>[<font style="color:rgb(55, 65, 81);">GitHub</font>](https://github.com/)<font style="color:rgb(55, 65, 81);">，并用您的账户登录。</font>
2. **导航到仓库**<font style="color:rgb(55, 65, 81);">： 在您的个人或组织页面中找到并点击您要删除分支的仓库。</font>
3. **进入分支页面**<font style="color:rgb(55, 65, 81);">： 在仓库页面，点击“Branches”标签，这通常位于页面的上方，靠近代码、issues 和 pull requests。</font>
4. **找到要删除的分支**<font style="color:rgb(55, 65, 81);">： 在“Branches”页面中，您会看到所有的分支。找到您想要删除的分支。</font>
5. **删除分支**<font style="color:rgb(55, 65, 81);">： 在要删除的分支右侧，您会看到一个垃圾桶图标（或 “Delete” 按钮）。点击它，确认删除。</font>

<h3 id="36c59bd7">方法 2：通过 Git 命令行删除分支</h3>
<font style="color:rgb(55, 65, 81);">如果您更喜欢使用命令行，也可以通过 Git 命令删除远程分支：</font>

1. **打开终端**<font style="color:rgb(55, 65, 81);">（Windows 使用 Git Bash、命令提示符或 PowerShell，macOS 和 Linux 使用终端）。</font>
2. **导航到您的本地仓库**<font style="color:rgb(55, 65, 81);">：</font>

```plain
bash复制代码
cd /path/to/your/repo
```

3. **删除远程分支**<font style="color:rgb(55, 65, 81);">： 使用以下命令删除远程仓库中的分支：</font>

```plain
bash复制代码
git push origin --delete <branch-name>
```

<font style="color:rgb(55, 65, 81);">示例：</font>

```plain
bash复制代码
git push origin --delete feature-branch
```

<h3 id="631cd220">确认删除</h3>
<font style="color:rgb(55, 65, 81);">无论采用哪种方法，您都可以通过再次查看分支列表来确认分支已成功删除。通过 GitHub 网站的“Branches”标签或使用以下命令查看当前的远程分支：</font>

```plain
bash复制代码
git branch -r
```

<font style="color:rgb(55, 65, 81);">这将列出所有远程分支，确认您要删除的分支不再显示。</font>

<font style="color:rgb(55, 65, 81);"></font>

<font style="color:rgb(55, 65, 81);"></font>

<h2 id="XCUPT"><font style="color:rgb(55, 65, 81);">7.合并分支</font></h2>
<h3 id="IQ05s">7.1详细的合并分支方法</h3>
```python
# 1. 获取所有远程分支
git fetch --all

# 2. 查看所有分支
git branch -a

# 3. 切换到主分支
git checkout main

# 4. 更新主分支
git pull origin main

# 5. 合并指定分支
git merge origin/feature_branch

# 6. 如果有冲突，解决冲突
# 编辑冲突文件
git add .
git commit -m "resolve conflicts"

# 7. 推送合并结果
git push origin main
```

<h3 id="RyDJj">7.3 使用rebase合并</h3>
```python
# 1. 切换到要合并的分支
git checkout feature_branch

# 2. 更新分支
git pull origin feature_branch

# 3. 执行 rebase
git rebase main

# 4. 切换回主分支
git checkout main

# 5. 合并分支
git merge feature_branch

# 6. 推送更改
git push origin main
```

