#!/usr/bin/env python3
"""Jeu: deviner le nombre.

Le programme demande un intervalle (borne inférieure et supérieure). Il choisit
aléatoirement un nombre secret dans cet intervalle. L'utilisateur saisit des
propositions et le programme répond "Trop petit", "Trop grand" ou "Bravo"
jusqu'à trouver la bonne valeur.

Usage:
    python guessing_game.py

Le texte est en français pour correspondre à la demande.
"""
from __future__ import annotations

import random
from typing import Tuple


def get_interval() -> Tuple[int, int]:
    """Demande à l'utilisateur deux entiers formant un intervalle [low, high].

    Retourne (low, high) avec low < high.
    """
    while True:
        try:
            raw_low = input("Borne inférieure (entier) : ").strip()
            low = int(raw_low)
            raw_high = input("Borne supérieure (entier, strictement > borne inférieure) : ").strip()
            high = int(raw_high)
            if low >= high:
                print("La borne supérieure doit être strictement supérieure à la borne inférieure. Réessayez.")
                continue
            return low, high
        except ValueError:
            print("Entrée invalide : veuillez saisir des entiers. Réessayez.")


def pick_secret(low: int, high: int) -> int:
    """Renvoie un nombre aléatoire dans l'intervalle inclusif [low, high]."""
    return random.randint(low, high)


def compare_guess(guess: int, secret: int) -> str:
    """Compare la proposition `guess` avec `secret`.

    Retourne:
      - 'small' si guess < secret
      - 'big' si guess > secret
      - 'correct' si guess == secret
    """
    if guess < secret:
        return "small"
    if guess > secret:
        return "big"
    return "correct"


def play_game(low: int, high: int, secret: int | None = None) -> int:
    """Lance la boucle principale du jeu.

    Si `secret` est None, il est choisi aléatoirement. Renvoie le nombre de tentatives.
    """
    if secret is None:
        secret = pick_secret(low, high)

    attempts = 0
    print(f"J'ai choisi un nombre entre {low} et {high}. Devinez-le !")
    while True:
        raw = input(f"Proposition (entre {low} et {high}) : ").strip()
        try:
            guess = int(raw)
        except ValueError:
            print("Veuillez entrer un entier valide.")
            continue
        if guess < low or guess > high:
            print("Votre proposition est en dehors de l'intervalle. Réessayez.")
            continue

        attempts += 1
        result = compare_guess(guess, secret)
        if result == "small":
            print("Trop petit.")
        elif result == "big":
            print("Trop grand.")
        else:
            print(f"Bravo ! Vous avez trouvé le nombre en {attempts} tentative(s).")
            return attempts


def main() -> None:
    print("Bienvenue au jeu du nombre à deviner !")
    low, high = get_interval()
    play_game(low, high)


if __name__ == "__main__":
    main()
