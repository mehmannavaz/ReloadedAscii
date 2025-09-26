# Idea
Let's draw a cube-head dude for now:
```
 ______ 
| _  _ |
||_||_||
|______|
```
here OUR cube-head dude and now it times to magic:
```
    ______       
   | _  _ |      
   ||_||_||      
   |______|      
                 
   __________    
  /         /\   
 /         /  \  
/_________/    \ 
\   _   _ \     \
 \ /_/\/_/\\    /
  \\_\/\_\/ \  / 
   \_________\/  
                 
                 
  __________     
 /         /\    
/_________/  \   
\   _   _ \   \  
 \ /_/\/_/\\   \ 
  \\_\/\_\/ \  / 
   \_________\/  
```
there is some size problem so let me explain what
## Space problem
it's look like for each 3x2 cube we create for dot in normat we need 4x3 spaces:
```
3x2
 _  < 
|_| <

^^^

4x3
 _   <
/_/\ <
\_\/ <

^^^^
```
### fix
we need to make the normal version big as turned version like this:
```
                   __________    
                  /         /\   
 __________      /         /  \  
|  __  __  |    /_________/    \ 
| |  ||  | |    \   _   _ \     \
| |__||__| |     \ /_/\/_/\\    /
|          |      \\_\/\_\/ \  / 
|__________|       \_________\/  
```
so much better