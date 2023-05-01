# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dgerwig- <dgerwig-@student.42urduli>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/15 16:23:20 by dgerwig-          #+#    #+#              #
#    Updated: 2023/04/15 16:55:51 by dgerwig-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


USER = dgerwig-

all: install

install:
	curl -LO "https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh"
	sh Miniconda3-latest-MacOSX-x86_64.sh -u /goinfre/$(USER)/miniconda3
	/goinfre/$(USER)/miniconda3/bin/conda init zsh
	/goinfre/$(USER)/miniconda3/bin/conda config --set auto_activate_base false
	source ~/.zshrc
	conda create --name 42AI-$(USER) python=3.7 jupyter pandas pycodestyle numpy
	conda info --envs

fclean:
	rm -rf Miniconda3-latest-MacOSX-x86_64.sh
