import justpy as jp


class Dictionary:
    path = "/dictionary"

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        div = jp.Div(a=wp, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="Instant English Dictionary", classes="text-4xl m-2")
        jp.Div(a=div, text="Get the definition of any English word instaltly as you type.", classes="text-lg")

        jp.Input(a=div, placeholder="Type in a word here...",
                 classes="m-2 bg-gray-100 border-2 boarder-gray-200 rounded w-64 focus:outline-none "
                         "focus:border-purple-500 focus:bg-white py-2 px-4")
        jp.Div(a=div, classes="m-2 p-2 text-lg border-2 h-40")


        return wp
