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

def sendPony(msg):
    sc = gotobot.getSC()
    sc.rtm_send_message(msg["channel"], random.choice(ponyArt))