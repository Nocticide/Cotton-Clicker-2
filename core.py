Let's make a game!
  name:Cotton Clicker 2
  by:Nocticide
  desc:rest in piece my man cotton clicker 1

Resources
  *Cotton
    name:Cotton
    desc:Rich, luscious, the gold of the natural world.

Upgrades
  *applePieRecipe 
    name:Apple pie recipe
    desc:Unlocks the ability to make apple pies!
    
  *cherryPieRecipe
    name:Cherry pie recipe
    desc:Boy, you'll never guess!

Buildings
  *brownCow
    name:Brown cow
    desc:A big friendly cow that generates 1 milk per second.   
    cost:20 coins
    on tick:give 1 Cotton

Buttons
 *pickCotton
  name:Pick cotton
  desc:Click to pick cotton. Gains 1 cotton.
  on click:yield 1 Cotton
    
