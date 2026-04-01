# Generating new themes

Here is an example conversation with Copilot to use one theme to make another. Then iterate with testing from that. 

```
Without changing any other code in any other files, can you look at the ./default.css and the ./dark-theme.css and track what changed between them. Then use those areas to create a new .css theme file like the ./defaults.css file with that structure I can use elsewhere that has the blue and green colors from https://www.soteriasoft.com/. Only change where there are colors referenced to create this new CSS file.  Every single CSS class that is in the ./default.css file must be in the newer ./openrmfpro-soteriasoft.css file. This is not an overlay this would be used as a replacement. I need to wholly replace the default.css with the openrmfpro-soteriasoft.css and have all CSS class names there to use for my application. 

For the body background color, can you make it the #05225a color.  As well as the navbar-glass for the menu. And the current .navbar-light .navbar-nav .nav-link make it an off white color show it shows well on the background color of #05225a.  And the badge-soft-cat1 needs to be a lighter shade of red than the badge-soft-critical class. The card-header class should have a thin light black border and the background color should be a lighter shade of blue from the #05225a color. And the And the badge-soft-cat1 needs to be lighter still.
```

```
The h1, h2, h3, h4, h5, h6, .h1, .h2, .h3, .h4, .h5, .h6 all need be an off white color to show better in the card-header class. 
```