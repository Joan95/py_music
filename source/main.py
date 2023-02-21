from wave import Wave


def main():
    w1 = Wave("C#0")
    w1.generate_wave()

    w2 = Wave("G#2")
    w2.generate_wave()

    w3 = Wave("Bb6")
    w3.generate_wave()
    pass


if __name__ == "__main__":
    main()
