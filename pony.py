import random
import gotobot
ponyArt = ["""                    ▄▄▄███████████████▄▄
                  ▅▀█████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████▄
                       ▄▄▄█████▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓███▄▄
                    ▄██▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓██▄     ▓▓
                 ▄█▒▒▓  ▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓██▓   ▓▓
              ▄█▒▒▒▒▒▓  ▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓       ▓
            ▄█▒▒▒▒▒▒▒▓ ▓   ▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓         ▓
          ▄█▒▒▒▒▒▒▒▒▒▓      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▓           ▓
         ██▒▒▒████▓▓▓▓▓    ▓    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓        ▓    ▓
        ███▀▀██▓▓▓▓▓▓▓▓▓ ▓       ▓▓▀▀▀▀▀▀██▓▓▓▓▓▓▓          ▓    ▓█
      █▀   ▄█▓▓▓▓▓▓▓▓▓▓▓▓        ▓       ██▓▓▓▓▓▓▓▓▓          ▓   ▓██
         ▄█▓▓▓▓▓▓▓▓█████▓▓              ██▓▓▓▓██▀▀▀▓          ▓   ▓▓▓█
       ▄█▓▓▓▓▓▓███▓███▓▓  ▓            █▓██▀▀▀                 ▓   ▓▒▓▓█
     ▄█▓▓▓▓▓███▒▒▓██▓██▓              █▀▀  ▓▓▓▓▓▓▓           ▓   ▓▒▒▓▓█
    ██▓▓▓███▒▒▒▒▓██▓▓██▓               ▓▓▓▓██████▓▓▀      ▓     ▓▒▒▒▓▓█
   █▓▓████▒▒▒▒▒▓██▓▓▒██▓            ▓▓███▒▒▓▓▓▓██▓             ▓▒▒▒▒▓▓█
  █▓█▀ ██▒▒▒▒▒▒▓██▓▒▒██▓          ▓▓██▒▒▒▒▓▓▓▓▓██▓▄▀         ▓▓▓▒▒▒▓▓█
 ██    ██▒▒▒▒▒▒▓██▒▒▓▓█▓▓        ▓▓██▓▒▒▒▓▓▓▓▓▓██▓          ▓█▓▓▒▒▒▒▓█
▀     ██▒▒▒▒▒▒▒▓██▒▒▓▓█▓▓       ▓▓██▓▓▓▒▒▒▓▓▓▓██▓▄▄▀      ▓ █▓▓▒▒▒▒▓▓█
     ██▒▒▒▒▒▒▒▒▓██▒▒▓▓█▓▓▓    ▓▓██▓▓▓▓▒▒▒▒▓▓▓██▓            █▓▓▒▒▒▒▒▓█
     ██▒▒▒▒▒▒▒▒▓██▒▒▒▓██████▓▓▓██▓▓▓▒▒▒▒▒▓▓▓██▓           █▓▓▓▒▒▒▒▒▓▓█
    ██▒▒▒▒▒▒▒▒▒▓██▒▓▓██▓▓▓▓▓████▓▓▓▒▒▒▒▒▓▓▓██▓           █▓▓▓▒▒▒▒▒▒▓▓█
    █▒▒▒▒▒▒▒▒▒▒▒▓█▓▓▓█▓▓      ▓▓█▓▓▒▒▒▒▒▓▓▓▓██▓           █▓▓▓▓▒▒▒▒▒▓▓█
   █▒▒▒▒▒▒▒▒▒▒▒▓▓█▓▓██▓       ▓▓█▓▓▒▒▒▒▓▓▓▓██▓           █▓▓▓▓█▒▒▒▒▒▓▓█
   █▒▒▒▒▒▒█▒▒▒▒▓▓▓▓▓▓          ▓▓█▓▒▒▒▒▓▓▓▓██▓           █▓▓▓▓█▒▒▒▒▒█▓▓█
  █▒▒▒▒▒▒█▒▒▒▒▓▓▓▓    ▄▄   ▄   ▓▓██▒▒▒▒▓▓███▓            █▓▓▓██▒▒▒▒▒██▓█
  █▒▒▒▒▒██▒▒▒▓▓▓▓▓▓        █▐   ▓▓████████▓▓            █▓▓▓█ █▒█▒▒▒█ █▓█
  █▒▒▒██ █▒▒▒▓▓▓▓▓▓▓▓▓▄▄▄▀ ▐    ▓▓▓▓███▓▓         ▓▓▓▓█▓▓█ █▒▒█▒▒▒█  ██
 █▒▒▒█   █▒▒▒▓▓▓▓▓▓▓▓▓▓     ▐        ▓▓▓▓        ▓▓▓   ████   █▒▒█▒▒█    █
 █▒▒█    █▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▄▀               ▓▓▓▓▓     ██      █▒▒██▒▒█    █
 █▒█      █▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                   █▒▒███▒█
 ██       █▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█                            █▒▒█ █▒█
 █         █▒▒▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▓▓█                             █▒█   █▒█
            █▒▓▓▓▓▓▓▓█▓▓▓▓▓██▓▓█                            █▒█     ██
            █▒▓▓▓▓▓▓▓██▓▓▓█  ███                            ██       █
             █▓▓▓▓▓▓▓█ █▓▓▓█   █                            █         ▀
              █▓▓▓▓▓▓█  █▓▓▓█
              █▓▓▓▓▓▓█   ██▓█
               █▓▓▓▓▓█      ██
                █▓▓▓▓▓█       █
                 █▓▓▓▓█
                  ██▓▓▓█
                    █▓▓▓█
                     ██▓▓█
                        ██
                          █""",


"""                                   ▄██▄
                                 ▄█▓▓█▒█▄
                                █▓▓▓▓█▒▒█▄
                              ▄█▓▓▓▓█▒▒▒▒█
                              █▓▓▓▓▓█▒▒▒▒█
  ▄▄▄▄▄▄▄                  █▓▓▓▓▓█▒▒▒▒▒█
 █▓▓▓▓▓▓▓██▄             █▓▓▓▓▓█▒▒▒▒▒▒█        ▄▄▄▄▄▄▄▄▄
 █▓▓▓▓▓▓▓▓▓▓███▄        █▓▓▓▓█▒▒▒▒▒▒▒█   ▄▄██▓▓▓▓▓▓▓▓██▄▄
█▒█▓▓▓▓▓▓▓▓▓▓▓▓▓██▄   █▓▓▓▓█▒▒▒▒▒▒▒█▄████████▓▓▓▓▓▓▓▓▓██▄
█▒▒█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▄ █▓▓▓█▒▒▒▒▒▒▒█▓▓▓▓▓▓▓▓▓██████▓▓▓▓▓▓█▄
 █▒▒▒█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓█▒▒▒▒▒▒████████████▓▓▓▓▓███▓▓█▓▓█
 █▒▒▒▒███▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▒░░░▒▒█▓▓▓▓▓▓▓▓▓▓▓▓███▓▓▓▓▓█▓█▓▓█
  █▒▒▒▒▒▒████▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░░░░▒▓▓▓▓▓▓▓▓▓██▓▓▓▓██▓▓▓▓█▓███
   █▒▒▒▒▒▒▒▒▒█████▓▓▓▓▓▓▓▓▒░▒░░░░▒█████▓▓▓▓▓██▓▓▓▓█▓▓▓▓██▓█
    █▒▒▒▒▒▒▒▒▒▒▒▒▒████████▒░▒░░░░░░░░░░██████░░██▓▓▓█▓▓▓▓▓█
     █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒░░░░░░░░░░░░░░░░░░░███▓█▓▓▓▓█▐
      █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒░░░░░░░░░░░░░░░░░░░░░███▓▓▓█▄▌▄
       █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░▌░▄▀▀███▄░░░░░░███▓ ▀▀▄
        ███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒░░░░░░░░█▄▄▀   ▓   ▀█▄░░░░░▌  █▓▀▀
            ████▒▒▒▒▒▒▒▒▒▒▒██   ▒▒░░░░░░░█    ▓     ███░░░░▐ ▄▀▓
                 ▀▀███████▀▀▀        ██░░▅▅▀      ▓    ████░░░▐███▓
                                        █▓█░░░░      ▓███▄▄██░░░░▓█▓ 
                                       █▓▓█░░░░       ▓█████▓░░░░▒▒▒
                                      █▓▓▓█░░░░        ▓▓██▓░░░░░▄▄░▒
                                     █▓▓▓▓▓█░░░░      ▒▒▒▒░░░░▐▄░░░▒
                                    ██▓▓▓▓▓▓█░░░░░▒▒▒░░░░░░░░▌▀▀▒
                                   █▓██▓▓█▓▓▓█▒▒░░░░░░░░░░░░░▀▒
                                   █▓█▓█▓▓███    ▒▒▒▒▒▒▒▒▒▒▒▒▒
                                  █▓▓█▓█▓▓▓██
                                   █▓▓█▓██▓▓▓█
                                    █▓▓█▓▓███▓█
                                     █▓▓▓█▓▓▓███
                                      █▓▓▓██▓▓▓█
                                       ████▓▓██
                                            ██""",
 
 
"""                          ▒▒▒▒▒▒▒▒▒▒          ▒▒▒▒▒▒
                      ▒▒▒▒▒░░░░░░░▒▒▒▒    ▒▒▒▒▒▒▒▒▒▒▒
                    ▒▒▒░░░░░░░░░░░░░░▒▒▒▒▒░░░░░░░░▒▒▒▒
                  ▒▒▒░░░░░░░░░░░░░░░░▒▒░░░░░░░░░░░░░▒▒▒
                 ▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓░░░░▒▒
                ▒▒▒░░░░░░▓▓▓▓░░░░░░░░░░░░░░░▓▓▓▓▓░░░░▒▒▒
                ▒▒▒░░░░░▓▓▓▓▓▓░░░░░░░░░░░░░░░▓▓▓▓░░░░▒▒▒▒▒▒▒▒▒
                ▒▒░░░░░░░▓▓▓▓░░░░░░░░░░░░░░░░░▓▓░░░░░▒▒▒▒░░░░▒▒▒▒
        ▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒
     ▒▒▒░░░░░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒
   ▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░░▒▒
  ▒▒▒░░░░░░░░░▓▓▓░░░░░░░░░░░░▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░▓▓▓▓░░░░░░▒▒
 ▒▒▒░░░░░░░░▓▓▓▓▓▓░░░░░░░░░░▓▓▓▓▓▓▓░░░░░░░▓▓▓░░░░░░░░▓▓▓░░░░░░▒▒
 ▒▒▒░░░░░░░░▓▓▓▓▓▓░░░░░░░░░░░▓▓▓▓▓░░░░░░░▓▓▓▓▓░░░░░░░░░░░░░░░░▒▒
  ▒▒▒░░░░░░░░░▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓░░░░░░░░░░░░░░░░▒▒
   ▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒
     ▒▒▒▒░░░░░░░░░░░░░░░░▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒
       ▒▒▒▒░░░░░░░░░░░░░▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒
         ▒▒░░░░░░░░░░░░░░░▓▓▓░░░░░░░░░░░░░░░░▓▓▓░░░░░░░░░░░░▒▒
         ▒▒▒░░░░░░░░░▒░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓░░░░░░░░░░░▒▒
          ▒▒▒░░░░░░░▒▒▒░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓░░░░░░░░░░░▒▒
            ▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░▒▒░░░░░░░░░░░░░░░░░░░▒▒
                    ██▓▓▓▒▒▒░░░░░░░░░░░░▒▒▒▒░░░░░░░░░░░░░░░░▒▒▒
                     ██▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░▒▒▒▒▒▒▒▒▒
                     ██▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒
                      ██▓▓▓▓▓▓█▓▓▓▓▓█▓▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓██
                      ██▓▓▓▓▓▓█▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▓▓█▓▓▓▓██
                       ██▓▓▓▓▓█▓▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▓█▓▓▓▓██
                        ██▓▓▓▓█▓▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▓█▓▓▓▓██
                        ██▓▓▓▓█▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓█▓▓▓▓▓██
                         ██▓▓▓▓█▓▓▓▓▓▓▓▓█▓▓▓▓▓▓█▓▓▓▓▓██
                         ██████████████████████████████""",
 
"""              ▄▄
              █▓█▄
               █▓▓█
                █▓██
                 █▓▓██
                  █▓█▓█
                   █▓▓▓█▄                      ▄
                    █▓█▓▓█                    ██
                     █▓▓▓▓█                 ▄███
                      █▓▓▓▓██              ████
                       █▓▓█▓▓█      ▄    ▄████
                        ██▓▓▓▓██   ██▄ ▄█████
                         █▓▓▓▓█▓█▄██████████
                          █▓▓█▓▓▓▓██████████▓▓▓
                           ██▓▓▓▓█▓▓█████████▒▒▓▓▓▓▓          ▄▄
                          ▓█▓▓▓▓▓█▓▓▓█████████████▒▒▓▓▓▓  ▄█▓▓█▄
                      ▓▓▓▒▒█▓▓▓█▓▓▓█▓▓████▒▒▒▒▒▒▒▓▒▒▒▒▒▓█▓▓▓▓▓█
                  ▓▓▓▒▒▒▒▒▒███▓▓▓█▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▒▒█▓▓▓▓▓▓▓█
                ▓▓▒▒▒▒▒▒▒▒▒█▓▓▓█▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▓▓▓▓▓▓█▓▓█
              ▓▓▒▒▒▒▒▒▒▒▒▒▒█▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓█▓▓█
            ▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓█▓▓█
          ▓▓▒▒▒▒▒▒▒▒▒▒▒▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▓█
         ▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█
        ▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓█▓
       ▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▓▓▓█▓▓▓▓▓▓▓▓█▒▓
      ▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒█▒▓▓▓█▓▓▓▓▓▓▒▓
     ▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒████████████▓▓▓▓█▓▓▒▒▓
     ▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒███▀▀        ▀██████▓▓▓▒▒▒▓
    ▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▒██▓▓▓▓           ▐▓▓▓▓▓▓▓▓▒▒▒▒▓
    ▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓██▓▓   ▓▓         ▐▓▓▓▓▓▓▓▓▒▒▒▒▓▓
    ▓▓▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓████     ▓▓         ▓▓▓▓▓▓▓▓▒▒▒▒▓▓
     ▓▓▒▒▒▒▒▒▒▒▒▒▒▓▓▓▒▒▒▓▓▓▓▓▓▓▓████▌     ▓▓       ▓▓▓▓▓▓▓▓▒▒▒▒▒▓▓
     ▓▓▒▒▒▒▒▒▒▒▒▒▒█▓▓▓▓▓▓▓▓▓▓▓▓▓██▀ ▐      ▓       ▓▓▓▓▓▓▓▓▒▒▒▒▒▓▓
      ▓▓▒▒▒▒▒▒▒▒▒█▓▓▓▓▓▓▓▓▓▓▓▓▓ ██▌  █▄   ▒▒      ▓▓▓▓▓▓▓▓▒▒▒▒▒▒▓▓
       ▓▓▒▒▒▒▒▒▒██▓▓▓▓▓▓▓▓▓▓▓▓▓  ███████▒▒▒    ▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▓▒▓
        ▓▓▒▒▒▒██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   █████▒▒▒   ▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▓▒▓
         ▓▓▒▒▒█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ▓██▓▓▓  ▓▓▓▓▓▓▓▓▓▓██▒▒▒▒▒▒▒▓▒▓
          ▓▓▒▒▒█▓▓▓▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▒▒▒▒▒▒▓▒▒▓
           ▓▓▒▒▒█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▒▒▒▒▒▒▓▒▒▓
            ▓▓▒▒▒███▓▓▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█████▓▓▓▓▓▒▒▒▒▒▒▒▓▒▒▓
             ▓▓▒▒▒▒▒███▓▓▓▓▓██████████████▒▒█▓▓▓▓▓▓▓▒▒▒▒▒▒▒▓▒▒▒▓
              ▓▓▒▒▒▒▒▒▒█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▓▓▓▓▓▒▒▒▒▒▒▒▓▒▒▒▓
               ▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▓▓▓▓▒▒▒▒▒▒▒▒▓▒▒▒▓
               ▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▓▓▓▒▒▒▒▒▒▒▒▓▒▒▒▓
               ▓▓▒▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓█▓▓▒▒▒▒▒▒▒▒▓▒▒▒▓
               ▓▓▒▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓ █▓▓▒▒▒▒▒▒▒▓▒▒▒▒▓
           ▓  ▓▒▒▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒▒▒▒▒▓▓  █▓▒▒▒▒▒▒▒▓▒▒▒▒▓
            ▓▓▒▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒▒▒▒▒▓     ▓▓▒▒▒▒▒▒▓▒▒▒▒▓
              ▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒▒▒▒▓▓       ▓▒▒▒▒▒▒▒▓▒▒▒▒▓
            ▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▓▓▓         ▓▒▒▒▒▒▒▓▒▒▒▒▒▓
                 ▓▓▓▓▓▓▒▒▒▒▒▓▓▓▓▓▓▓▓▓             ▓▒▒▒▒▒▓▒▒▒▒▓
                        ▓▓▓▓▓▓                         ▓▓▒▒▒▓▒▒▒▒▓
                                                           ▓▓▒▒▓▒▒▒▒▓
                                                              ▓▓▒▒▒▒▒▓          ▓
                                                                ▓▒▒▒▒▒▓          ▓▓
                                                                ▓▒▒▒▒▒▓         ▓▒▓
                                                                 ▓▓▒▒▒▒▓▓     ▓▒▒▒▓
                                                                   ▓▒▒▒▒▒▒▓▓▓▓▒▒▒▓
                                                                    ▓▒▒▒▒▒▒▒▒▒▒▒▒▓
                                                                     ▓▓▒▒▒▒▒▒▒▒▒▓
                                                                        ▓▓▓▓▓▓▓▓▓""",


"""                           ▓▓▓
                       ▓▓▓▒▒▒▓
                    ▓▓▒▒▒▒▒▒▒▓      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
                  ▓▓▒▒▓▓▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
                ▓▓▒▒▒▓▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓       ▓▓▓▓▓▓▓
               ▓▓▒▒▒▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓       ▓▓▓▓▓
             ▓▓▒▒▒▒▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓      ▓▓
            ▓▓▒▒▒▒▓▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓
           ▓▓▒▒▒▒▓▒▒▒▒▒▒▒▒▒▓░░░░░░▓▓▓▓▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓
          ▓▒▒▒▒▒▓▒▒▒▒▒▒▒▒▒▓░░░░░░░░░▓▓▓▓▒▒▒▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓
          ▓▒▒▒▒▒▓▒▒▒▒▒▒▒▒▒▓▓░░░░░░░░░▓▓▓▓▓▒▒▒▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓
          ▓▒▒▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▓░░░░░░░░░░▓▓▓▓▓▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓
          ▓▒▒▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▓░░░░░▒░░░░░▓▓▓▓▓▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓
         ▓▓▒▒▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓░░░▒░░░░░▓▓▓▓▓▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓
        ▓▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓░░░▒░░░░░░▓▓▓▓▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓
       ▓▒▒▓▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▓░░▒▒░░░░░░▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▓
      ▓▒▒▒▓▒▒▒▒▒▄▒▒▒█▄▀▀▀▀▀▄▄▒▒▒▒▒▒▓▒▒▒░░░░░░░▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓ ▓▒▓
     ▓▒▒▒▒▓▒▒▒▒▒▀▄▄▀            ▀▄▒▒▒▒▓▒▒▒░░▓░░░░░▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▓ ▓▒▓
    ▓▒▒▒▒▓▒▒▒▒▄▒▄▀                 █▒▒▒▓▓▒▒░▓▒▓░░░░░▓▓▓▒▒▒▒▒▒▒▒▒▒▒▓  ▓▒▓
    ▓▒▒▒▓▓▒▒▒▒▒██          ▓▓▓▓▓▓▓▓▒▒▒▓▓▒▒▓▒▒▓░░░░░▓▓▓▒▒▒▒▒▒▒▒▒▒▓   ▓▒▓
   ▓▒▒▒▓▓▓▒▒▒▒▒█         ▓▓▓▓▓▓▓▓▓▓▒▒▒▓▓▒▓▒▒▒▓░░░░░▓▓▓▒▒▒▒▒▒▒▒▒▒▓   ▓▒▓
  ▓▒▒▓▓▓▓▓▒▒▒▒▒        ▓▓▓▓▓       █▒▒▒▒▓▒▓▒▒▒▒▓░░░░░▓▓▓▒▒▒▒▒▒▒▒▒▓     ▓
  ▓▒▓▓▓▓▓▓▒▒▒▒▒       ▓▓▓▓▓       ▄█▒▒▒▒▒▓▒▒▒▒▒▓░░░░░▓▓▓▒▒▒▒▒▒▒▒▒▓
  ▓▓▓▓▓▓▓▓▒▒▒▒▒      ▓▓▓▓▓      ▄███▒▒▒▒▒▒▒▒▒▒▒▓░░░░░░▓▓▒▒▒▒▒▒▒▒▓
  ▓▓▓▓▓▓▓▓▒▒▒▒▒      ▓▓▓▓██▄▄▄████▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓░░░░░▓▓▒▒▒▒▒▒▒▓
  ▓▓▓▓▓▓▓▓▓▒▒▒▒▒     ▓▓▓▓████   ██▒▒▒▒▒▒▒▒▒▓▓▓    ▓░░░░░▓▓▒▒▒▒▒▒▓
  ▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒    ▓▓▓▓████▄▄██▒▒▒▒▒▒▒▒▓▓▓    ██▓░░░░░░▓▒▒▒▒▒▒▓
 ▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒    ▓▓▓▓███████▒▒▒▒▒▒▒▒▓▓▓  ▄███  ▓▓░░░░░▓▒▒▒▒▒▓
  ▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒   ▓▓▓▓█████▒▒▒▒▒▒▒▒▒▓▓ █▀▀██      ▓▓░░░░▒▒▒▒▒▓
  ▓▓▓▓▓▓▓▓▓▒▓▒▒▒▒▒▒▒  ▓▓▓▓▓███▒▒▒▒▒▒▒▒▒▒▓▓█▄▄█           ▓▓▓░▒▒▒▒▒▓
  ▓▓▓▓▓▓▓▓▓▒▒▓▒▒▒▒▒▒▒▒▒▒▓▓▓▒▒▒▒▒▒▒▒▒▒▓▒▒▓███                 ▓▓▓▒▒▒▒▓
   ▓▓▓▓▓▓▓▓▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒██                       ▓▓▓▒▓
    ▓▓▓▓▓▓▓▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓                          ▓▓
    ▓▓▓▓▓▓▓▒▒▒▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▓
     ▓▓▓▓▓▓▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒░▓▓▓▒▒▒▒▒▒▒▒▒▒▓
      ▓▓▓▓▓▒▒▒▒▒▒▒▒▒▓▓▓▒▒▒▒▒▒▒░░▓▓▓▓▓▒▒▒▒▓▓▓
       ▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▒▒▒▒░░░▓▓▓▓
         ▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓░▓▓▒▒▒░░░▓
          ▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓░░▓▓▓▓▒▒▓▓
            ▓▒▒▒▒▒▒▒▒▒▒▒▓░░░▒▒▓▓▓▒▓▓
            ▓▒▒▒▒▒▒▒▒▒▒▓░░░▒▒▓▒▒▒▓▓▓
             ▓▒▒▒▒▒▒▒▒▓░░░▒▒▒▓▒▒▒▓▓▓▓
             ▓▒▒▒▒▒▒▒▓░░▒▒▒▒▓▒▒▒▓▓▓▓
             ▓▒▒▒▒▒▒▓░░▒▒▒▒▓▒▒▒▓▓▓▓▓
              ▓▒▒▒▒▓░░▒▒▒▓▓▒▒▒▓▓▓▓▓▓
              ▓▒▒▒▓░░▒▒▒▓▓▒▒▒▓▓▓▓▓▓
               ▓▒▓░░▒▒▒▓▒▒▒▓▓▓▓▓▓▓
                ▓▓░▒▒▓ ▓▒▒▒▓▓▓▓▓▓
                ▓░░▒▓ ▓▒▒▒▓▓▓▓▓▓
                 ▓░▒▓ ▓▒▒▓▓▓▓▓▓
                  ▓▒▓ ▓▒▓▓▓▓▓
                   ▓▓ ▓▓▓▓▓▓
                       ▓▓▓▓▓
                        ▓▓▓
                        ▓▓
                         ▓""",
 
"""         ▄          ▄▄▄▄
       ▄██      ▄▄██▀      ▄▄▄▄
      █▓▓█   ▄█▓▓█▀  ▄███▓▓▓▓██▄
     ▐▓▓▓█ █▓▓▓█ ▄██▓▓▓▓▓▓▓▓▓▓▓██▄
     ▐▓▓▓██▓▓▓▓██▓▓▓▓▓▓▒▒▒▓▓███▀▀▀▄
  ▄  ▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▓▓▓▓██▄
 ▐▓▌ ▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▓▒▒▓▓▓▓▓██▄
 ▐▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▒▒▒▒▓▒▒▓▓▓▓▓▓▓█
  ▐▓▓▓█▓▓▓▓▓▓▓▓▓████▒▒▓▒▒▒▒▓▒▒▓▓▓▓▓▓▓█
   █▓▓▓▓▓▓▓▓▓▓██▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒▓▓▓█▀▀▀█
    ▀█▓▓▓▓▓▓██▒▒▒▒▒▒▒▒▒▒▒▄▒▒▒▓▒▒▓▓▓▓█
       ██▓▓█▒▒▒▒▒▒▒▒▒▒▒▒▄▀▒▒▒▒▒▒▓▓▓▓▓▓█
     ▄█▓█▓█▒▒▒▒▒▄▒▒▒▒▒▄▀▀▄▒▒▒▒▒▓▒▓▓▓▓▓▓█
   ▄█▀▄██▒▒▒▒▒▒▒▌▒▒▄█▀   ██▒▒▒▒▒▒▒▓▓▓▓▓▓█
   █  ██▒▒▒▒▒▒▒▒▐▄█▓▓███▄██▒▒▒▒▒▒▒▓▓▓█▀██
      █▓▄▀▀▄▒▒▒▒▒▀  ▓▓█████▒▒▒▒▒▒▒▒▓▓▓▓█ ▐
      ▌ ▓ ▄▄▌▒▒▒▒▒   ▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▓▓▓▓█
         ▓ ██▒▒▒▒▒▒     ▓▓▓▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓█
          ▓ ▓▒▒▒▒▒▒▒▒▒▒▒▒▒▄▀▀▀▄▒▒▒▒▒▒▓▓█▓▓█
         ▓▓▒▄▒▒▒▒▒▒▒▒▒▄▀▀▄▄░░░▌▓▒▒▒▒▒▓▓█▓█
        ▓▓▒▒▒▒▒▒▄▄▄▄██ ▀▀ ▄▀▀▀▓▒▒▒▒▒▒▓▓█ █
          ▓▓▒▒▄▀▒ ███▀▀▀▀▀▒▒▓▓▒▒▒▒▒▒▒▓▓█  ▌
        ▄▄▀▀▀   ▄▄▀▒▒▒▒▓▓▓▓▓▒▒▒▒▒▒▒▒▒▓▓█
      ▄█ ▒▄▄▀▀▀▓▓▒▒▓▓▓ ▓▒▒▒▒▒▒▒▒▒▒▒▒▒▓█
       ▀▀▀         ▓▓     ▓▒▒▒▒▒▒▒▒▒▒▒▓▓ █
                          ▓▓▒▒▒▒▒▒▒▒▒▓▓     ▓
                        ▓  ▓▒▒▒▒▒▓▓▓▓      ▓
                       ▓▓ ▓▒▒▓▓▓          ▓
                       ▓  ▓▒▓ ▄▓         ▓
                       ▓ ▐▓▓▓█▓▓      ▓▓
                       ▓▓▐▓▓▓█▀▓  ▓▓▓
                       ▓  ███   ▓▓▓
                         ▐▓█▓▌
                         ▐▓█▓▌
                         ▐▓▓▓▓█
                          █▓▓▓▓█
                           █▓▓█
                            ██
                             ▀""",
 
"""                                             ▄▄████████▄
                                           ▄█▓▓▓█▓▓▓▓▓▓██▄
                                           █▓▓▓▓▓██▓▓▓▓▓▓▓█▄
                                ▄█████▄ █▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓█
                ▄▄██████████▓▓▓▓▓▓▓██▓▓▓▓▓▓▓█▓▓▓▓▓▓▓██
             ▄█▓▓▓▓▓▓▓▓▓▓█▓██▓▓▓▓▓▓▓█▓▓▓▓▓█▓▓▓▓▓▓▓█▓█
          ▄█▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▓█▓▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓▓█▓▓█
        ▄█▓▓▓▓▓▓▓▓▓▓▓▓▓▓████▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓▓██▓▓█
       █▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▓███▓▓▓▓█
      █▓▓▓▓▓▓▓▓▓▓▓▓███▀▀▀▀██▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▓▓█▓▓▓▓█  ▄████████▄
     █▓▓▓▓▓▓▓▓▓▓█▀▀           ▀█▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓█▓▓▓███▓▓▓▓▓▓▓▓▓▓█▄
    █▓▓▓▓▓▓▓▓▓█▀               ▓▓█▓▓▓▓███████▓███▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓█
    █▓▓▓▓▓▓▓▓█             ▓▓▓░░░█▓██░░░░░░░███▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▓▓▓▓█
     █▓▓▓▓▓▓█            ▓▓░░░░░░██░░░░░░░░░░░░███▓░░░░░░░░░▓▓▓▓▓▓▓▓▓▓█
  █▌ █▓▓▓▓▓█           ▓░░░░░░░░░░░░░░░░░░░░░░░░▓░░░░░░░▓░░▓▓▓▓▓▓▓▓▓▓▓█
 █▓█ █▓▓▓▓█          ▓▄▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓░░░▓▓▓▓▓▓▓▓▓▓▓█
█▓▓▓██▓▓▓█         ▓█░░▐░░░░░░░░░▄█████▄░░░░░░░░░░░░░▓░░░░▓▓▓▓▓▓▓▓▓▓▓█
█▓▓▓▓▓▓▓█        ▀▄█░░░▐░░░░░░▄█▀░░░░░░▀█░░░░░░░░░░░▓░░░░▓▓▓▓█▓▓▓▓████
 ██▓▓▓██        ▀▀▄▌░░░▐░░░░░░█░░░░░░░░░░█░░░░░░░░░▓░░░░░▓▓▓▓█▓███▓▓▓█
   ▀▀▀▀          ▀▄█░░░░▐░░░░░█░░░░░░░░░░░▐▌░░░░░░░▓░░░░░▓▓▓▓█▓▓▓▓▓▓▓█
                  ▓░░▓▓▓▓░░░░░░█░░░░░░░░░░░░▐▄▄▄▅░░░░░░░░░▓████▓▓▓▓▓▓▓█
                 ▓░░▀░░░░░░░░░░▀░░░░░░░░░░░░▐▀▄▄▅░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓█
                  ▓░░░░░░░░░░░░░░░░░░░░░░░░░░▀▄▄░░░░░░░░█▓▓▓▓▓▓▓▓▓▓▓█
                   ▓░░░░░▓▓▓░░░░░░░░░░░░░░░░░░░░░███████▓▓▓▓▓▓▓▓▓▓▓█
                    ▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██
                       ▓▓▓▓▓░░░░░░░░░░░░░░░░░░█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████
                       ▓▓▓▓▓░░░░░░░░░░░░░░░░░█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓█
                       ▓▓▓▓▓░░░░░░░░░░░░░░░░░█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▓█
                       ▓▒▒▓░░░░░░░░░░░░░░░░░░░█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▓█
                     ▓▓▒▓░░░░░░░░░░░░░░░░░░░████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▓█
                      ▓▓▓▓▓░░░░░░░░░░░░░░███▓▓▓▓█▓▓▓██▓▓▓▓██▓▓▓▓▓█▓▓▓█
                             ▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▓█▓▓█▓▓▓▓█▓█████▓▓▓▓█
                                           █▓▓▓▓▓▓▓▓▓▓▓███▓▓▓▓█▓▓▓▓▓▓▓▓▓▓█
                                          █▓▓▓▓▓▓▓▓████▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▓▓█
                                         █▓▓▓▓▓▓▓▓▓▓█▓▓██████▓▓▓▓▓▓▓▓▓█
                                         █▓▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▓▓▓▓███
                                          █▓▓▓▓▓▓▓▓▓▓▓█▓▓▓▓███████
                                           █▓▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓█
                                            █▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓█
                                          ███████████▓▓▓▓▓▓▓▓█
                                         █▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█
                                        █▓▓▓▓▓██▓▓▓▓▓▓▓▓██
                                         █▓▓▓▓▓▓█▀▀▀▀▀▀▀
                                           ██▓▓▓▓███▄▄
                                              ▀▀▀▀▀""",
 
"""                                  ▄█▀▄
                     ▄▀▀▀▄   ▄█▀░▌░░▀▀▄▀▀█▀▄
                   ▄▀▄▀▀▄░▀▀░▐░░█▀▀▄▐░░▄▀░░▐
             ▄▄▄▄  ▀     ▀▀▀▀▀▀▀   ▐▐░░▐░▄▀▀▀▀▀▀▄
            ▀▄▄▄ ▀▄     ▄▀▀▄▄       ▀▀▀█▀░░░▄▀▀▀▐
          ▄     ▀▄ ▀▄    ▀▀▄▄ ▀▀▄      █░░▄▀░░▄▄█
         ▀▄▀▄    ▀▄ ▐        ▀▀▄  ▀▄   █░▄▀░▄▀░░▌
           ▀▄▀▄   ▐  ▐           ▀▌  █  ▀▀▄▄█▄▄▀▀▀▀▄▄       ▄▄
 █▄         ▄▀▄▀▀▀   ▀▀▀▀▀▀▄▄▄▄▌  ▐▀▀▄▄▄  ▄▀░░░▄▀▀▀▌  ▄▀ ▄█▄
 ▀▄▀▄    ▄▀ █  ▄▄▀▀▀▀▀▀▀▀▄▄      ▐█▄    ▀█▄░░▄▀░▄▀▀▐ ▌  ▀   ▀▄
   ▀▄ ▀▀▀▄▀█▒█               ▀▀▄▄▄▀          ▀▀▄▄▀░░░▄▀      ▀█▀▀
      ▀▀▀   ▐▒▒█                 ▄▀                 ▀▄░░▌  ▄▀▀▀▄ ▐
              ▐▒▒█▄             █ ▄           ▄▀▀▀▄  ▐▒▒▌ ▐▒▒▒▒▀▄▐
               ▐▒▒▒███▄▄▄▄▄▄▀▄▀▌     ▌  ▄▀▒▒▒▒▒▀▄ ▐▒▌ ▐▒▓▓▓▓▒▒▌
                ▐█▒▒▒▒▒▒▒▒▒▒▒▒▒▌ ▐ ▐▒▌▐▒▒▒▒▓▓▓▓▓▒▌▐▌ ▐▓▄▀▄▓▓▒▌
                 ▀█████████████ ▐▒▌▐▒▌▐▒▒▒▓▓▓▓▓▓▓▓▌▐ ▐▓▌  ▀▄▓▒▌
                   ▀█░░░░░░░░░░█░░▌▐▒▒█▒▒▒▓▓▓▌▀▀▀▄▓▓▌▐▓▌    ▐▓▒█
                     ▀█░░░░░░░░░░█▀▀    ▐▒▒▓▓▓▌     ▀▄▓█▓▓▌  ▓▓▐▓▒▌
                       ▀█░░░░░░█▀        ▐▒▒▒▓▓▌     ▓ ▐▓▓▒▓  ▓ ▓▓▓▒▌
                          ▀▀▀▀▀▀          ▐▒▒▒▒▓▓▌    ▓  ▓▓▓▒▓  ▓ ▓▓▒▌
                                            ▐▒▒▒▒▒▓▓     ▓▓▓▓▓▒▒▓▓▓▓▒█
                                             ▐▒▒▒▒▒▓▓      ▓▓▓▓▒▒▒▒▒▒▌
                                             ▐▒▒▒▒▒▒▓▓▓     ▓▓▒▒▒▒▒▒▌
                                              ▐▒▒▒▒▒▒▒▓▓▓▓▓▓▒▒▒▒▒▒▒▌
                                               ▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌      ▄
                                                ▀█▒▒▒▒▒▒█▀▀▀█▒▒▒▒▒▒▒▌    ▐▒▌
                                                   ▀▀▀▀▀▀      ▀█▒▒▒▒▒▀▀▀▀█▒█▄▄
                                                                  ▐▒█▒▒▒▒▀▀▄▐▒▌▒▒█▄
                                                                  ▐▒█▒▒▒▒█▀▐▒▀▒▄▀
                                                                  ▐▒▌▌▒▒▒▒▀▒▒▄▀▌
                                                                  ▐▒▌▐▒▒▒▒▒▄▀▌ ▌
                                                                  ▐▒▐ ▀▀▀█▀  ▐▐
                                                                  ▐▒▒▀▄▄▄█    ▐
                                                                  ▐▒▒▒▒▒▒▒▀▄  ▀▄
                                                                  ▐▒▒▒▒▒▒▒▄▀▀▄ ▀▄
                                                                   ▀▄▄▄▄▄▀     ▀▀"""]
class Pony:
    def sendPony(bot, msg):
        bot.sc.rtm_send_message(msg["channel"], random.choice(ponyArt))

    def getPony():
      return random.choice(ponyArt)