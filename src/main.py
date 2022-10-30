import music_bot, discord_version, environment_variables


def main():
    discord_version.show_discord_version()
    environment_variables.load_environment_variables()
    music_bot.run_music_bot()


if __name__ == "__main__":
    main()
