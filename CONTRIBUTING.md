## Contributing to heapExchange

 ***   The world can only really be changed one piece at a time. 
   The art is picking that piece.

    — Tim Berners-Lee ***

There are many ways you can contribute to heapExchange.
 We'd like it to be a community-led project

### Pull requests

It's a good idea to make pull requests early on. 
A pull request represents the start of a discussion, and doesn't necessarily need to be the final, finished submission.

It's also always best to make a new branch before starting work on a pull request.
 This means that you'll be able to later switch back to working on another separate issue without interfering with an ongoing pull requests.

It's also useful to remember that if you have an outstanding pull request then pushing new commits to your GitHub repo will also automatically update the pull requests.

GitHub's documentation for working on pull requests is [available here](https://help.github.com/articles/using-pull-requests)

Always run the tests before submitting pull requests, and ideally run tox in order to check that your modifications are compatible on all supported versions of Python and Django.

Once you've made a pull request take a look at the Travis build status in the GitHub interface and make sure the tests are running as you'd expect.

### Managing compatibility issues

Sometimes, in order to ensure your code works on various different versions of Django, Python or third party libraries, you'll need to run slightly different code depending on the environment. Any code that branches in this way should be isolated into the compat.py module, and should provide a single common interface that the rest of the codebase can use.
