---
title: Contributing to Angular 为 Angular 做贡献
date created: 星期四, 二月 16日 2023, 2:50:01 下午
date modified: 星期四, 二月 16日 2023, 3:51:00 下午
---

> [!info] angular 规范

# Contributing to Angular 为 Angular 做贡献

We would love for you to contribute to Angular and help make it even better than it is today! As a contributor, here are the guidelines we would like you to follow:  
我们希望您能为 Angular 做出贡献，并帮助它比今天更好！作为贡献者，以下是我们希望您遵循的准则：

-   [Code of Conduct 行为准则](https://github.com/angular/angular/blob/main/CONTRIBUTING.md#coc)
-   [Question or Problem?  有疑问还是问题？](https://github.com/angular/angular/blob/main/CONTRIBUTING.md#question)
-   [Issues and Bugs  问题和错误](https://github.com/angular/angular/blob/main/CONTRIBUTING.md#issue)
-   [Feature Requests  功能请求](https://github.com/angular/angular/blob/main/CONTRIBUTING.md#feature)
-   [Submission Guidelines  提交指南](https://github.com/angular/angular/blob/main/CONTRIBUTING.md#submit)
-   [Coding Rules  编码规则](https://github.com/angular/angular/blob/main/CONTRIBUTING.md#rules)
-   [Commit Message Guidelines  提交消息准则](https://github.com/angular/angular/blob/main/CONTRIBUTING.md#commit)
-   [Signing the CLA  签署 CLA](https://github.com/angular/angular/blob/main/CONTRIBUTING.md#cla)

## Code of Conduct 行为准则

Help us keep Angular open and inclusive. Please read and follow our [Code of Conduct](https://github.com/angular/code-of-conduct/blob/main/CODE_OF_CONDUCT.md).  
帮助我们保持 Angular 的开放性和包容性。请阅读并遵守我们的行为准则。

## Got a Question or Problem? 有疑问或问题？

Do not open issues for general support questions as we want to keep GitHub issues for bug reports and feature requests. Instead, we recommend using [Stack Overflow](https://stackoverflow.com/questions/tagged/angular) to ask support-related questions. When creating a new question on Stack Overflow, make sure to add the tag.`angular`  
不要为一般支持问题打开问题，因为我们希望保留 GitHub 问题以用于错误报告和功能请求。相反，我们建议使用堆栈溢出来询问与支持相关的问题。在堆栈溢出上创建新问题时，请确保添加标签。 `angular`

Stack Overflow is a much better place to ask questions since:  
堆栈溢出是一个更好的提问场所，因为：

-   there are thousands of people willing to help on Stack Overflow  
    有成千上万的人愿意在堆栈溢出上提供帮助
-   questions and answers stay available for public viewing so your question/answer might help someone else  
    问题和答案仍可供公众查看，因此您的问题/答案可能会对其他人有所帮助
-   Stack Overflow's voting system assures that the best answers are prominently visible.  
    Stack Overflow 的投票系统确保最佳答案清晰可见。

To save your and our time, we will systematically close all issues that are requests for general support and redirect people to Stack Overflow.  
为了节省您和我们的时间，我们将系统地关闭所有请求一般支持的问题，并将人们重定向到 Stack Overflow。

If you would like to chat about the question in real-time, you can reach out via [our Discord server](https://discord.gg/angular).  
如果您想实时讨论该问题，可以通过我们的联系 不和谐服务器 .

## Found A Bug? 发现了错误？

If you find a bug in the source code, you can help us by [submitting an issue](https://github.com/angular/angular/blob/main/CONTRIBUTING.md#submit-issue) to our [GitHub Repository](https://github.com/angular/angular). Even better, you can [submit a Pull Request](https://github.com/angular/angular/blob/main/CONTRIBUTING.md#submit-pr) with a fix.  
如果您在源代码中发现错误，您可以通过将问题提交到我们的 GitHub 存储库来帮助我们。更好的是，您可以提交带有修复程序的拉取请求。

## Missing A Feature? 缺少功能？

You can _request_ a new feature by [submitting an issue](https://github.com/angular/angular/blob/main/CONTRIBUTING.md#submit-issue) to our GitHub Repository. If you would like to _implement_ a new feature, please consider the size of the change in order to determine the right steps to proceed:  
您可以通过向我们的 GitHub 存储库提交问题来请求新功能。如果您想实现新功能，请考虑更改的大小，以确定正确的步骤：

-   For a **Major Feature**, first open an issue and outline your proposal so that it can be discussed. This process allows us to better coordinate our efforts, prevent duplication of work, and help you to craft the change so that it is successfully accepted into the project.  
    对于主要功能，首先打开一个问题并概述您的建议，以便可以讨论它。此过程使我们能够更好地协调我们的工作，防止重复工作，并帮助您制定更改，以便将其成功接受到项目中。
    
    **Note**: Adding a new topic to the documentation, or significantly re-writing a topic, counts as a major feature.  
    注意：向文档添加新主题或大量重写主题都算作一项主要功能。
    
-   **Small Features** can be crafted and directly [submitted as a Pull Request](https://github.com/angular/angular/blob/main/CONTRIBUTING.md#submit-pr).  
    可以制作小功能并直接作为拉取请求提交。
    

## Submission Guidelines 提交指南

### Submitting An Issue 提交问题

Before you submit an issue, please search the issue tracker. An issue for your problem might already exist and the discussion might inform you of workarounds readily available.  
在提交问题之前，请搜索问题跟踪器。您的问题可能已经存在，讨论可能会告知您随时可用的解决方法。

We want to fix all the issues as soon as possible, but before fixing a bug, we need to reproduce and confirm it. In order to reproduce bugs, we require that you provide a minimal reproduction. Having a minimal reproducible scenario gives us a wealth of important information without going back and forth to you with additional questions.  
我们希望尽快修复所有问题，但在修复错误之前，我们需要重现并确认它。为了重现错误，我们要求您提供最少的重现。拥有最少的可重现场景为我们提供了丰富的重要信息，而无需向您提出其他问题。

A minimal reproduction allows us to quickly confirm a bug (or point out a coding problem) as well as confirm that we are fixing the right problem.  
最少的复制使我们能够快速确认错误（或指出编码问题）并确认我们正在修复正确的问题。

We require a minimal reproduction to save maintainers' time and ultimately be able to fix more bugs. Often, developers find coding problems themselves while preparing a minimal reproduction. We understand that sometimes it might be hard to extract essential bits of code from a larger codebase, but we really need to isolate the problem before we can fix it.  
我们需要最少的复制，以节省维护者的时间，并最终能够修复更多的错误。通常，开发人员在准备最小复制时会自己发现编码问题。我们知道，有时可能很难从更大的代码库中提取必要的代码，但我们确实需要在修复问题之前隔离问题。

Unfortunately, we are not able to investigate / fix bugs without a minimal reproduction, so if we don't hear back from you, we are going to close an issue that doesn't have enough info to be reproduced.  
不幸的是，我们无法在没有最少重现的情况下调查/修复错误，因此如果我们没有收到您的回复，我们将关闭一个没有足够的信息来重现的问题。

You can file new issues by selecting from our [new issue templates](https://github.com/angular/angular/issues/new/choose) and filling out the issue template.  
您可以通过从我们的新问题模板中进行选择并填写问题模板来提交新问题。

### Submitting A Pull Request (PR)

提交拉取请求 （PR）

Before you submit your Pull Request (PR) consider the following guidelines:  
在提交拉取请求 （PR） 之前，请考虑以下准则：

1.  Search [GitHub](https://github.com/angular/angular/pulls) for an open or closed PR that relates to your submission. You don't want to duplicate existing efforts.  
    在 GitHub 中搜索与您的提交相关的开放或封闭 PR。您不想重复现有的工作。
    
2.  Be sure that an issue describes the problem you're fixing, or documents the design for the feature you'd like to add. Discussing the design upfront helps to ensure that we're ready to accept your work.  
    确保问题描述了您要修复的问题，或记录了要添加的功能的设计。预先讨论设计有助于确保我们已准备好接受您的工作。
    
3.  Please sign our [Contributor License Agreement (CLA)](https://github.com/angular/angular/blob/main/CONTRIBUTING.md#cla) before sending PRs. We cannot accept code without a signed CLA. Make sure you author all contributed Git commits with email address associated with your CLA signature.  
    请在发送 PR 之前签署我们的贡献者许可协议 （CLA）。我们不能接受没有签名 CLA 的代码。确保使用与 CLA 签名关联的电子邮件地址创作所有贡献的 Git 提交。
    
4.  [Fork](https://docs.github.com/en/github/getting-started-with-github/fork-a-repo) the angular/angular repo.  
    分叉角度/角度存储库。
    
5.  In your forked repository, make your changes in a new git branch:  
    在分支仓库中，在新的 git 分支中进行更改：
    
    git checkout -b my-fix-branch main
    
6.  Create your patch, **including appropriate test cases**.  
    创建补丁，包括适当的测试用例。
    
7.  Follow our [Coding Rules](https://github.com/angular/angular/blob/main/CONTRIBUTING.md#rules).  
    遵循我们的编码规则。
    
8.  Run the full Angular test suite, as described in the [developer documentation](https://github.com/angular/angular/blob/main/docs/DEVELOPER.md), and ensure that all tests pass.  
    运行完整的 Angular 测试套件，如开发人员文档中所述，并确保所有测试都通过。
    
9.  Commit your changes using a descriptive commit message that follows our [commit message conventions](https://github.com/angular/angular/blob/main/CONTRIBUTING.md#commit). Adherence to these conventions is necessary because release notes are automatically generated from these messages.  
    使用遵循我们的提交消息约定的描述性提交消息提交更改。遵守这些约定是必要的，因为发行说明是根据这些消息自动生成的。
    
    git commit --all
    
    Note: the optional commit command line option will automatically "add" and "rm" edited files.`-a`  
    注意：可选的提交命令行选项将自动“添加”和“rm”编辑的文件。 `-a`
    
10.  Push your branch to GitHub: 将您的分支推送到 GitHub：
    
    git push origin my-fix-branch
    
11.  In GitHub, send a pull request to .`angular:main`  
    在 GitHub 中，向 发送拉取请求。 `angular:main`
    

### Reviewing A Pull Request 查看拉取请求

The Angular team reserves the right not to accept pull requests from community members who haven't been good citizens of the community. Such behavior includes not following the [Angular code of conduct](https://github.com/angular/code-of-conduct) and applies within or outside of Angular managed channels.  
Angular 团队保留不接受来自不是社区好公民的社区成员的拉取请求的权利。此类行为包括不遵守 Angular 行为准则，并且适用于 Angular 托管渠道内部或外部。

#### Addressing Review Feedback 处理审阅反馈

If we ask for changes via code reviews then:  
如果我们通过代码审查要求更改，那么：

1.  Make the required updates to the code.  
    对代码进行所需的更新。
    
2.  Re-run the Angular test suites to ensure tests are still passing.  
    重新运行 Angular 测试套件以确保测试仍然通过。
    
3.  Create a fixup commit and push to your GitHub repository (this will update your Pull Request):  
    创建一个修正提交并推送到您的 GitHub 存储库（这将更新您的拉取请求）：
    
    git commit --all --fixup HEAD
    git push
    
    For more info on working with fixup commits see [here](https://github.com/angular/angular/blob/main/docs/FIXUP_COMMITS.md).  
    有关使用修正提交的更多信息，请参阅此处 。
    

That's it! Thank you for your contribution!  
就是这样！感谢您的贡献！

##### Updating The Commit Message 更新提交消息

A reviewer might often suggest changes to a commit message (for example, to add more context for a change or adhere to our [commit message guidelines](https://github.com/angular/angular/blob/main/CONTRIBUTING.md#commit)). In order to update the commit message of the last commit on your branch:  
审阅者可能经常建议对提交消息进行更改（例如，为更改添加更多上下文或遵守我们的提交消息准则）。要更新分支上最后一次提交的提交消息：

1.  Check out your branch: 查看您的分行：
    
    git checkout my-fix-branch
    
2.  Amend the last commit and modify the commit message:  
    修改上次提交并修改提交消息：
    
    git commit --amend
    
3.  Push to your GitHub repository: 推送到您的 GitHub 存储库：
    
    git push --force-with-lease

> NOTE:  
> If you need to update the commit message of an earlier commit, you can use in interactive mode. See the [git docs](https://git-scm.com/docs/git-rebase#_interactive_mode) for more details.  
> 如果需要更新早期提交的提交消息，可以在交互模式下使用。有关更多详细信息，请参阅 git 文档。`git rebase`

#### [](https://github.com/angular/angular/blob/main/CONTRIBUTING.md#after-your-pull-request-is-merged)After Your Pull Request is Merged

合并拉取请求后

After your pull request is merged, you can safely delete your branch and pull the changes from the main (upstream) repository:  
合并拉取请求后，您可以安全地删除分支并从主（上游）存储库中提取更改：

-   Delete the remote branch on GitHub either through the GitHub web UI or your local shell as follows:  
    通过 GitHub Web UI 或本地 shell 删除 GitHub 上的远程分支，如下所示：
    
    git push origin --delete my-fix-branch
    
-   Check out the main branch: 查看主要分支：
    
    git checkout main -f
    
-   Delete the local branch: 删除本地分支：
    
    git branch -D my-fix-branch
    
-   Update your local with the latest upstream version:`main`  
    使用最新的上游版本更新本地版本： `main`
    
    git pull --ff upstream main
    

## [](https://github.com/angular/angular/blob/main/CONTRIBUTING.md#-coding-rules)Coding Rules 编码规则

To ensure consistency throughout the source code, keep these rules in mind as you are working:  
为了确保整个源代码的一致性，请在工作时牢记以下规则：

-   All features or bug fixes **must be tested** by one or more specs (unit-tests).  
    所有功能或错误修复都必须通过一个或多个规范（单元测试）进行测试。
    
-   All public API methods **must be documented**.  
    必须记录所有公共 API 方法。
    
-   We follow [Google's JavaScript Style Guide](https://google.github.io/styleguide/jsguide.html), but wrap all code at **100 characters**.  
    我们遵循谷歌的 JavaScript 风格指南，但将所有代码包装为 100 个字符。
    
    An automated formatter is available, see [DEVELOPER.md](https://github.com/angular/angular/blob/main/docs/DEVELOPER.md#clang-format).  
    可以使用自动格式化程序，请参阅 DEVELOPER.md 。
    

## [](https://github.com/angular/angular/blob/main/CONTRIBUTING.md#-commit-message-format)Commit Message Format 提交消息格式

_This specification is inspired by and supersedes the [AngularJS commit message format](https://docs.google.com/document/d/1QrDFcIiPjSLDn3EL15IJygNPiHORgU1_OOAqWjiDU5Y/edit#).  
此规范受到 AngularJS 提交消息格式的启发并取代了该格式。_

We have very precise rules over how our Git commit messages must be formatted. This format leads to **easier to read commit history**.  
我们对 Git 提交消息的格式有非常精确的规则。这种格式使提交历史记录更易于阅读。

Each commit message consists of a **header**, a **body**, and a **footer**.  
每个提交消息都由标头、正文和页脚组成。

```
<header>
<BLANK LINE>
<body>
<BLANK LINE>
<footer>
```

The is mandatory and must conform to the [Commit Message Header](https://github.com/angular/angular/blob/main/CONTRIBUTING.md#commit-header) format.`header`  
这是必需的，必须符合提交消息标头格式。 `header`

The is mandatory for all commits except for those of type "docs". When the body is present it must be at least 20 characters long and must conform to the [Commit Message Body](https://github.com/angular/angular/blob/main/CONTRIBUTING.md#commit-body) format.`body`  
对于除“docs”类型的提交之外的所有提交都是必需的。当正文存在时，它必须至少为 20 个字符，并且必须符合提交消息正文格式。 `body`

The is optional. The [Commit Message Footer](https://github.com/angular/angular/blob/main/CONTRIBUTING.md#commit-footer) format describes what the footer is used for and the structure it must have.`footer`  
是可选的。提交消息页脚格式描述了页脚的用途及其必须具有的结构。 `footer`

### [](https://github.com/angular/angular/blob/main/CONTRIBUTING.md#commit-message-header)Commit Message Header 提交消息头

```
<type>(<scope>): <short summary>
  │       │             │
  │       │             └─⫸ Summary in present tense. Not capitalized. No period at the end.
  │       │
  │       └─⫸ Commit Scope: animations|bazel|benchpress|common|compiler|compiler-cli|core|
  │                          elements|forms|http|language-service|localize|platform-browser|
  │                          platform-browser-dynamic|platform-server|router|service-worker|
  │                          upgrade|zone.js|packaging|changelog|docs-infra|migrations|ngcc|ve|
  │                          devtools
  │
  └─⫸ Commit Type: build|ci|docs|feat|fix|perf|refactor|test
```

The and fields are mandatory, the field is optional.`<type>``<summary>``(<scope>)`  
和字段是必填字段，字段是可选的。 `<type>` `<summary>` `(<scope>)`

#### [](https://github.com/angular/angular/blob/main/CONTRIBUTING.md#type)Type

Must be one of the following:  
必须是以下之一：

-   **build**: Changes that affect the build system or external dependencies (example scopes: gulp, broccoli, npm)  
    生成：影响生成系统或外部依赖项的更改（示例范围：gulp、西兰花、npm）
-   **ci**: Changes to our CI configuration files and scripts (examples: CircleCi, SauceLabs)  
    ci：对 CI 配置文件和脚本的更改（例如：CircleCi、SauceLabs）
-   **docs**: Documentation only changes 文档：仅文档更改
-   **feat**: A new feature 壮举：新功能
-   **fix**: A bug fix 修复：错误修复
-   **perf**: A code change that improves performance  
    perf：提高性能的代码更改
-   **refactor**: A code change that neither fixes a bug nor adds a feature  
    重构：既不修复错误也不添加功能的代码更改
-   **test**: Adding missing tests or correcting existing tests  
    test：添加缺失的测试或更正现有测试

#### [](https://github.com/angular/angular/blob/main/CONTRIBUTING.md#scope)Scope

The scope should be the name of the npm package affected (as perceived by the person reading the changelog generated from commit messages).  
范围应该是受影响的 npm 包的名称（由读取从提交消息生成的更改日志的人员所感知）。

The following is the list of supported scopes:  
以下是支持的范围列表：

-   `animations`
-   `bazel`
-   `benchpress`
-   `common`
-   `compiler`
-   `compiler-cli`
-   `core`
-   `elements`
-   `forms`
-   `http`
-   `language-service`
-   `localize`
-   `platform-browser`
-   `platform-browser-dynamic`
-   `platform-server`
-   `router`
-   `service-worker`
-   `upgrade`
-   `zone.js`

There are currently a few exceptions to the "use package name" rule:  
目前，“使用包名称”规则有一些例外：

-   `packaging`: used for changes that change the npm package layout in all of our packages, e.g. public path changes, package.json changes done to all packages, d.ts file/format changes, changes to bundles, etc.  
    `packaging` ：用于更改我们所有软件包中的 npm 包布局的更改，例如公共路径更改、对所有包所做的 package.json 更改、d.ts 文件/格式更改、捆绑包更改等。
    
-   `changelog`: used for updating the release notes in CHANGELOG.md  
    `changelog` ：用于更新 CHANGELOG.md 中的发行说明
    
-   `dev-infra`: used for dev-infra related changes within the directories /scripts and /tools  
    `dev-infra` ：用于目录 /scripts 和 /tools 中的开发基础设施相关更改
    
-   `docs-infra`: used for docs-app (angular.io) related changes within the /aio directory of the repo  
    `docs-infra` ：用于存储库的 /aio 目录中的文档应用程序 （angular.io） 相关更改
    
-   `migrations`: used for changes to the migrations.`ng update`  
    `migrations` ：用于更改迁移。 `ng update`
    
-   `ngcc`: used for changes to the [Angular Compatibility Compiler](https://github.com/angular/angular/blob/main/packages/compiler-cli/ngcc/README.md)  
    `ngcc` ：用于更改角度兼容性编译器
    
-   `ve`: used for changes specific to ViewEngine (legacy compiler/renderer).  
    `ve` ：用于特定于 ViewEngine（旧版编译器/渲染器）的更改。
    
-   `devtools`: used for changes in the [browser extension](https://github.com/angular/angular/blob/main/devtools/README.md).  
    `devtools` ：用于更改浏览器扩展。
    
-   none/empty string: useful for and changes that are done across all packages (e.g. ) and for docs changes that are not related to a specific package (e.g. ).`test``refactor``test: add missing unit tests``docs: fix typo in tutorial`  
    none/空字符串：对所有包（例如）和与特定包无关的文档更改（例如）有用。 `test` `refactor` `test: add missing unit tests` `docs: fix typo in tutorial`
    

#### [](https://github.com/angular/angular/blob/main/CONTRIBUTING.md#summary)Summary

Use the summary field to provide a succinct description of the change:  
使用摘要字段提供更改的简洁描述：

-   use the imperative, present tense: "change" not "changed" nor "changes"  
    使用祈使式，现在时：“改变”不是“改变”也不是“改变”
-   don't capitalize the first letter  
    不要将第一个字母大写
-   no dot (.) at the end  
    末尾没有点 （.）

### [](https://github.com/angular/angular/blob/main/CONTRIBUTING.md#commit-message-body)Commit Message Body 提交消息正文

Just as in the summary, use the imperative, present tense: "fix" not "fixed" nor "fixes".  
就像在摘要中一样，使用祈使式，现在时：“修复”不是“固定”也不是“修复”。

Explain the motivation for the change in the commit message body. This commit message should explain _why_ you are making the change. You can include a comparison of the previous behavior with the new behavior in order to illustrate the impact of the change.  
在提交消息正文中解释更改的动机。此提交消息应说明进行更改的原因。您可以包括以前行为与新行为的比较，以说明更改的影响。

### [](https://github.com/angular/angular/blob/main/CONTRIBUTING.md#commit-message-footer)Commit Message Footer 提交消息页脚

The footer can contain information about breaking changes and deprecations and is also the place to reference GitHub issues, Jira tickets, and other PRs that this commit closes or is related to. For example:  
页脚可以包含有关中断性更改和弃用的信息，也可以引用 GitHub 问题、Jira 票证以及此提交关闭或与之相关的其他 PR。例如：

```
BREAKING CHANGE: <breaking change summary>
<BLANK LINE>
<breaking change description + migration instructions>
<BLANK LINE>
<BLANK LINE>
Fixes #<issue number>
```

or

```
DEPRECATED: <what is deprecated>
<BLANK LINE>
<deprecation description + recommended update path>
<BLANK LINE>
<BLANK LINE>
Closes #<pr number>
```

Breaking Change section should start with the phrase "BREAKING CHANGE: " followed by a summary of the breaking change, a blank line, and a detailed description of the breaking change that also includes migration instructions.  
中断性变更部分应以短语“中断性变更：”开头，后跟中断性变更的摘要、空白行和中断性变更的详细说明，其中还包括迁移说明。

Similarly, a Deprecation section should start with "DEPRECATED: " followed by a short description of what is deprecated, a blank line, and a detailed description of the deprecation that also mentions the recommended update path.  
同样，弃用部分应以“已弃用：”开头，后跟已弃用内容的简短说明、空行以及弃用的详细说明，其中还提到了建议的更新路径。

## [](https://github.com/angular/angular/blob/main/CONTRIBUTING.md#revert-commits)Revert Commits 还原提交

If the commit reverts a previous commit, it should begin with , followed by the header of the reverted commit.`revert:`  
如果提交还原了以前的提交，则应以 开头，后跟还原提交的标头。 `revert:`

The content of the commit message body should contain:  
提交消息正文的内容应包含：

-   information about the SHA of the commit being reverted in the following format: ,`This reverts commit <SHA>`  
    有关按以下格式还原的提交的 SHA 的信息：， `This reverts commit <SHA>`
-   a clear description of the reason for reverting the commit message.  
    对还原提交消息的原因的清晰描述。