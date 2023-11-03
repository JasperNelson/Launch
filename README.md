# Launch
Launch is a small python script that automates switching from starship prompt and the normal Oh-My-Zsh prompt
It has support for zshrc files stored in the $ZDOTDIR as well as the default $HOME directory.
To propery utlize this script you will want to add an alias to your zshrc file formatted like this:   

```alias launch='source *Directory*/.zshrc && python *Directory*/launch.py "${plugins[@]}"'```   

Example:   

```alias launch='source $ZDOTDIR/.zshrc && python /usr/local/bin/launch.py "${plugins[@]}"'```
