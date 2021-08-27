import justpy as jp


class Home:
    path = "/"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)
        div = jp.Div(a=wp, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="This is the Home page!", classes="text-4xl m-2")
        jp.Div(a=div, text="""
           Donec eget elit at ante malesuada auctor at non sem. Nullam rutrum dapibus dignissim. 
           Donec rhoncus euismod ex sit amet consequat. Pellentesque vitae leo libero. Phasellus gravida libero 
           convallis massa pharetra posuere. Curabitur turpis lacus, blandit at suscipit a, pulvinar sed lacus. Quisque 
           lacus sem, maximus et tempor et, rhoncus vel neque. Aliquam eget mi viverra, dictum diam sed, aliquet ligula. 
           Sed in lectus et velit auctor cursus at ut metus. Duis in euismod eros, vel ullamcorper erat. Fusce et 
           dapibus eros. Integer commodo eleifend nulla, ut molestie nisi ultrices quis. Mauris vulputate, 
           velit scelerisque pharetra volutpat, urna dui mattis ex, eu porta enim mi sed leo. 
           """, classes="text-lg")
        return wp
