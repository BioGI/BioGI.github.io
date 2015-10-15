---
title: How to install scholdoc 
author: Ganesh Vijayakumar
date: 13 Oct 2015
---

I have used the [Scholarly Markdown format](http://scholarlymarkdown.com/) and [scholdoc](http://scholdoc.scholarlymarkdown.com/), a fork of [Pandoc](http://pandoc.org/) to create these webpages. One of the main reasons for choosing this was having the native ability to [scale images](http://scholarlymarkdown.com/Scholarly-Markdown-Guide.html#floating-subfigs) and having internal references to them in the text. This originally seemed fairly complicated, so here's a sub-list of steps I followed

* I had to install `cabal-install` and `ghc` (apparently stands for Glasgow Haskell Interpreter). You might need to be `root` for this

```bash
apt-get install cabal-install ghc
```

* Then, as a normal user, I used them to install scholdoc as 

``` bash
cabal update
cabal install scholdoc
cabal install scholdoc-citeproc
```

* Download the supporting files from the example folder. Type `make`. If you followed all steps so far, this should work. 

 _If you got this to work, you don't need to do anything else. If you're still interested, read further._

* You might notice the web page style is not the same as the one on the scholdoc website. I didn't like the smallish container area for the theme. Hence I had to install the theme he had used at [https://github.com/timtylin/Heuristically-scholmd-theme](https://github.com/timtylin/Heuristically-scholmd-theme). I changed the pixel width to 1500 in the `variables.less` file, as I was going to use this theme primarily on large screen monitors with over 1300px resolution in the horizontal. 

``` 
// Large screen / wide desktop
@container-large-desktop:      ((1500px + @grid-gutter-width));
//** For `@screen-lg-min` and up.
@container-lg:                 @container-large-desktop;
```

* It turns out, it's not quite easy to get this theme recompiled. I followed instructions on the wiki. I had to install more stuff.. yay! 

``` bash
apt-get install npm
npm install -g grunt-cli
npm install -g bower
```

* Also, I **hate** the Heuristica font. I prefer the default `serif` font on my computer, the beautiful Georgia. So I just removed any mention of it from the css file it generated. Did I mention that the font and the theme on the [Pandoc website](http://www.pandoc.org) are __awesome__ ? Hint: It uses the default serif __Georgia__ on my firefox!

