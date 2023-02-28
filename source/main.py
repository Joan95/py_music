from wave import Wave
import notes


def main():

    for key in notes.notes_sounds.keys():
        for note in notes.notes_sounds[key]:
            print(f"{note}{key}")
            w = Wave(f"{note}{key}")
            w.generate_wave()


if __name__ == "__main__":
    main()
