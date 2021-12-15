import random
print("now you  have entered THE stone,paper and scissor game.Enjoy your game ")
print("STONE:")
print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

print("PAPER:")
print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

print("SCISSORS:")
print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
a=input("enter your choice ")
l=["stone","paper","scissor"]
b=random.choice(l)
print(b)
if a==b:
    print("its a draw as the computer chose",b)
elif a=="stone" and b=="paper":
    print("defeated as the computer chose ",b)
    print(''' 

                  BETTER LUCK NEXT TIME 
                   .___
                   @...V;
                  P:   :|
             .___"d `~" P.
            .@ .."W     d;
            :P'  "d     j#
             \@`_#f  ~  W.
               " #;    .@.",
                 P.     Pj n|
                 @.     #;  ":
                 n; ~   mZ   :;
                 M.    .#     f.
            ___.f#     .".   .d
          ."    ":     .";    ;f
     .____P     L.      :     jh
     h    "     |      //  ;Y
    "P    |    .nm    -j:     :P.
     W   .n                    .Y
     Z                        #8.
    .P                         'Z
     `f                       fj
      ":                      :d
       :p                    P;
        `v                  -l'
    ''')

elif a=="stone" and b=="scissor":
    print("won as the computer chose ", b)
    print('''$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$'`$$$$$$$$$$$$$'`$$$
$$$$$$  $$$$$$$$$$$  $$$$
$$$$$$$  '$/ `/ `$' .$$$$
$$$$$$$$. i  i  /! .$$$$$
$$$$$$$$$.--'--'   $$$$$$
$$^^$$$$$'        J$$$$$$
$$$   ~""   `.   .$$$$$$$
$$$$$e,      ;  .$$$$$$$$
$$$$$$$$$$$.'   $$$$$$$$$
$$$$$$$$$$$$.    $$$$$$$$
$$$$$$$$$$$$$     $$$$$$$''')
elif a=="paper" and b=="scissor":
    print("defeated as the computer chose ", b)
    print(''' 
               
              BETTER LUCK NEXT TIME 
               .___
               @...V;
              P:   :|
         .___"d `~" P.
        .@ .."W     d;
        :P'  "d     j#
         \@`_#f  ~  W.
           " #;    .@.",
             P.     Pj n|
             @.     #;  ":
             n; ~   mZ   :;
             M.    .#     f.
        ___.f#     .".   .d
      ."    ":     .";    ;f
 .____P     L.      :     jh
 h    "     |      //  ;Y
"P    |    .nm    -j:     :P.
 W   .n                    .Y
 Z                        #8.
.P                         'Z
 `f                       fj
  ":                      :d
   :p                    P;
    `v                  -l'
''')

elif a=="paper" and b=="stone":
    print("won as the computer chose ", b)
    print('''$$$$$$$$$$$$$$$$$$$$$$$$$
    $$$$$$$$$$$$$$$$$$$$$$$$$
    $$$$$'`$$$$$$$$$$$$$'`$$$
    $$$$$$  $$$$$$$$$$$  $$$$
    $$$$$$$  '$/ `/ `$' .$$$$
    $$$$$$$$. i  i  /! .$$$$$
    $$$$$$$$$.--'--'   $$$$$$
    $$^^$$$$$'        J$$$$$$
    $$$   ~""   `.   .$$$$$$$
    $$$$$e,      ;  .$$$$$$$$
    $$$$$$$$$$$.'   $$$$$$$$$
    $$$$$$$$$$$$.    $$$$$$$$
    $$$$$$$$$$$$$     $$$$$$$''')
elif a=="scissor" and b=="stone":
    print("defeated as the computer chose ", b)
    print(''' 

                  BETTER LUCK NEXT TIME 
                   .___
                   @...V;
                  P:   :|
             .___"d `~" P.
            .@ .."W     d;
            :P'  "d     j#
             \@`_#f  ~  W.
               " #;    .@.",
                 P.     Pj n|
                 @.     #;  ":
                 n; ~   mZ   :;
                 M.    .#     f.
            ___.f#     .".   .d
          ."    ":     .";    ;f
     .____P     L.      :     jh
     h    "     |      //  ;Y
    "P    |    .nm    -j:     :P.
     W   .n                    .Y
     Z                        #8.
    .P                         'Z
     `f                       fj
      ":                      :d
       :p                    P;
        `v                  -l'
    ''')

elif a=="scissor" and b=="paper":
    print("won as the computer chose ", b)
    print('''$$$$$$$$$$$$$$$$$$$$$$$$$
    $$$$$$$$$$$$$$$$$$$$$$$$$
    $$$$$'`$$$$$$$$$$$$$'`$$$
    $$$$$$  $$$$$$$$$$$  $$$$
    $$$$$$$  '$/ `/ `$' .$$$$
    $$$$$$$$. i  i  /! .$$$$$
    $$$$$$$$$.--'--'   $$$$$$
    $$^^$$$$$'        J$$$$$$
    $$$   ~""   `.   .$$$$$$$
    $$$$$e,      ;  .$$$$$$$$
    $$$$$$$$$$$.'   $$$$$$$$$
    $$$$$$$$$$$$.    $$$$$$$$
    $$$$$$$$$$$$$     $$$$$$$''')
else:
    print("the given input is not recognised by the computer please enter from stone paper and scissor ")
