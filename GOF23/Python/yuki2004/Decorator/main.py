from classes import *

if __name__ == '__main__':
    d1 = StringDisplay("Hello, world.")
    d2 = SideBorder(d1, "#")
    d3 = FullBorder(d2)


    d4 = SideBorder(
            FullBorder(
                FullBorder(
                    SideBorder(
                        FullBorder(StringDisplay("hello."))
                        ,"*"
                    )
                )
            )
            ,"/"
        )

    d1.show()
    d2.show()
    d3.show()
    d4.show()