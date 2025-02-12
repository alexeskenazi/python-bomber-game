a# Final Project Milestone II

*Place this document in your final project repo folder `/etc`. *

***

Come up with interfaces for 3 possible classes you think you may need for your project. Again, brainstorm a little. Nothing is *wrong*.

## Class Interface 1

class Character
  attributes:
    visible
    x
    y
    width
    height
    image
    health
    powerups

  methods:
    reset()
    move_right()
    move_left()
    shoot()
    add_health()
    loose_health()
    add_powerup()
    use_powerup()
    jump()


## Class Interface 2

class Bomb
  attributes:
    visible
    x
    y
    width
    height
    image
    damage
    speed
    
  methods:
    reset()
    move_down()
    explode()


## Class Interface 3

class Powerup
  attributes:
    visible
    x
    y
    width
    height
    image
    type
    speed
    
  methods:
    reset()
    move_down()
    catch()
    activate()

## Class Interface 4

class Scoreboard
  attributes:
    visible
    x
    y
    width
    height
    image
    lives
    score
    max_score
    
    
  methods:
    reset()
    add_life()
    increase_score()
