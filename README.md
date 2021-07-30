# MacroPact
## rPico KMK powered macropad with IPS screen
![MacroPact](/img/finished1.jpg)
Idea/Desing: [Sean Yin](https://www.coroflot.com/sean_yin/profile)

Build/Coding: [kbjunky](https://github.com/kbjunky) ( In case of any problems hit me up on **Discord kbjunky#6476** or **Reddit /u/kbjunky**)

## **BOM**
|Item                                       |Count|Example|
|:---                                       |:---:|:---:|
|USB-C Female Breakout                      |1|[Link](https://www.aliexpress.com/item/4000314458731.html?spm=a2g0o.productlist.0.0.5fc34d38lyT0Dp&algo_pvid=bcc1cc44-d24a-45d0-9bc5-987888faddf1&aem_p4p_detail=2021072423494813891420020531900015357713&algo_exp_id=bcc1cc44-d24a-45d0-9bc5-987888faddf1-0)|
|28AWG 10 Pin Flat Ribbon cable (Rainbow)   |5m|[Link](https://www.aliexpress.com/item/4000512709968.html?spm=a2g0o.productlist.0.0.a1aa3503ZKJAk9&algo_pvid=f8420484-4057-4393-8598-2d7b5b90c93d&algo_exp_id=f8420484-4057-4393-8598-2d7b5b90c93d-0)|
|M2/4mm heat insert                         |8|[Link](https://www.aliexpress.com/item/4000232858343.html?spm=a2g0o.productlist.0.0.744c388bzpfmK2&algo_pvid=b730dfaa-adef-48bd-9c4c-6387c7b94556&algo_exp_id=b730dfaa-adef-48bd-9c4c-6387c7b94556-0)|
|Raspberry Pico                             |1|[Link](https://sg.rs-online.com/web/p/raspberry-pi/2122162/)|
|WS2812 RGB Strip                           |min 7 diodes|[Link](https://www.aliexpress.com/item/2036819167.html?spm=a2g0o.productlist.0.0.76c874cauoQVho&algo_pvid=fdeec7a4-5fae-426a-8993-e6341adc3cab&algo_exp_id=fdeec7a4-5fae-426a-8993-e6341adc3cab-2)|
|240x240 IPS/TFT 1.3" screen                |1|[Link](https://www.aliexpress.com/item/32914468153.html?spm=a2g0o.productlist.0.0.2e233718vnQs0e&algo_pvid=bfdf2fcd-f326-4817-aad5-5e5e639df674&algo_exp_id=bfdf2fcd-f326-4817-aad5-5e5e639df674-13)|
|12mm Rotary Encoder with switch            |2|[Link](https://sg.rs-online.com/web/p/mechanical-rotary-encoders/7377742/)|
|Kailh Choc V1 Switch                       |17|[Link](https://kailh.aliexpress.com/store/4670072?spm=a2g0o.store_pc_groupList.pcShopHead_12560924.0)|
|Choc V1 Keycaps                            |17|[Link](https://kailh.aliexpress.com/store/4670072?spm=a2g0o.store_pc_groupList.pcShopHead_12560924.0)|
|1N4148 Fast switching diode through hole   |19|[Link](https://www.aliexpress.com/item/32729204179.html?spm=a2g0o.detail.1000023.37.5b88e47dXeHixn)|
|0.1mm copper jumper wire                   |1|[Link](https://www.aliexpress.com/item/32848033421.html?spm=a2g0o.productlist.0.0.494a1553LgDudN&algo_pvid=38dbe147-1108-472d-aff1-d27e6126209c&algo_exp_id=38dbe147-1108-472d-aff1-d27e6126209c-2)|
|M2/4mm flat head screw                     |4|[Link](https://www.aliexpress.com/item/10000181218734.html?spm=a2g0o.productlist.0.0.6020582dfAOH2E&algo_pvid=249be230-5d20-47ee-bfab-177bfda0f1ef&algo_exp_id=249be230-5d20-47ee-bfab-177bfda0f1ef-1)|
|M2/8mm flat head screw                     |4|[Link](https://www.aliexpress.com/item/10000181218734.html?spm=a2g0o.productlist.0.0.6020582dfAOH2E&algo_pvid=249be230-5d20-47ee-bfab-177bfda0f1ef&algo_exp_id=249be230-5d20-47ee-bfab-177bfda0f1ef-1)|
|15x16 Knob                                 |1|[Link](https://www.aliexpress.com/item/1005001323668563.html?spm=a2g0o.detail.1000014.23.248e794eVvCEnx&gps-id=pcDetailBottomMoreOtherSeller&scm=1007.14976.204930.0&scm_id=1007.14976.204930.0&scm-url=1007.14976.204930.0&pvid=a1382086-ef33-42ef-a9ab-94a2c085269f&_t=gps-id:pcDetailBottomMoreOtherSeller,scm-url:1007.14976.204930.0,pvid:a1382086-ef33-42ef-a9ab-94a2c085269f,tpp_buckets:668%230%23131923%2371_668%23888%233325%231_4976%230%23204930%239_4976%232711%237538%23796_4976%233104%239653%236_4976%234052%2321623%2388_4976%233141%239887%234_668%232846%238109%231935_668%232717%237564%23648_668%231000022185%231000066059%230_668%233422%2315392%23340_4452%230%23189847%230_4452%233474%2315675%23228_4452%234862%2322449%23630_4452%233098%239599%23666_4452%233564%2316062%23426)|
|25x17 Knob                                 |1|[Link](https://www.aliexpress.com/item/1005001323668563.html?spm=a2g0o.detail.1000014.23.248e794eVvCEnx&gps-id=pcDetailBottomMoreOtherSeller&scm=1007.14976.204930.0&scm_id=1007.14976.204930.0&scm-url=1007.14976.204930.0&pvid=a1382086-ef33-42ef-a9ab-94a2c085269f&_t=gps-id:pcDetailBottomMoreOtherSeller,scm-url:1007.14976.204930.0,pvid:a1382086-ef33-42ef-a9ab-94a2c085269f,tpp_buckets:668%230%23131923%2371_668%23888%233325%231_4976%230%23204930%239_4976%232711%237538%23796_4976%233104%239653%236_4976%234052%2321623%2388_4976%233141%239887%234_668%232846%238109%231935_668%232717%237564%23648_668%231000022185%231000066059%230_668%233422%2315392%23340_4452%230%23189847%230_4452%233474%2315675%23228_4452%234862%2322449%23630_4452%233098%239599%23666_4452%233564%2316062%23426)|
|6x2 antislip pads                          |4|[Link](https://www.aliexpress.com/item/1005001834060269.html?spm=a2g0o.productlist.0.0.1b4de9abYDw7VQ&algo_pvid=7e52f7bd-74d2-497d-89a9-5126675db393&algo_exp_id=7e52f7bd-74d2-497d-89a9-5126675db393-11)|

On top of that you'll be needing:
* Soldering iron
* Rosin core solder wire (anything between 0.5mm to 1mm, preferable with lead 'Pb')
* Sharp tool to remove supports from 3D printed parts
* Wire stripper but a normal knife will also do the job 
* [Hot glue gun](https://www.aliexpress.com/item/1005001393578323.html?spm=a2g0o.productlist.0.0.30283cf9bNBeBF&algo_pvid=874a8176-6f37-49d3-bb75-4a4656cfd7f0&algo_exp_id=874a8176-6f37-49d3-bb75-4a4656cfd7f0-1)
* [Soldering flux](https://www.aliexpress.com/item/32828595199.html?spm=a2g0o.productlist.0.0.f7cb377fEQC0uC&algo_pvid=7c56fd1b-76bf-451a-b90b-2ee1365edd5c&algo_exp_id=7c56fd1b-76bf-451a-b90b-2ee1365edd5c-0) or [flux marker](https://www.aliexpress.com/item/32828595199.html?spm=a2g0o.productlist.0.0.f7cb377fEQC0uC&algo_pvid=7c56fd1b-76bf-451a-b90b-2ee1365edd5c&algo_exp_id=7c56fd1b-76bf-451a-b90b-2ee1365edd5c-0)

### **Remarks**
Be sure to order same shaft type encoder/knob. Either Knurl or Flat(D-Type).

0.1mm copper wire is used to wire the switch matrix. It's enameled so there's no risk of shorting when crossed at the same time being very easy to solder unlike tranformer core enameled wires.

Keycaps can be ordered from Kailh Official store on [Aliexpress](https://kailh.aliexpress.com/store/4670072?spm=a2g0o.home.1000002.3.650c2145xJL0oJ). A better alternative is [MKUltra Set](https://mkultra.click/mbk-choc-keycaps).

Use flux on wires before soldering the tip.

# **Build guide**
### *Setup CircuitPython*

Follow [this](https://circuitpython.org/board/raspberry_pi_pico/) guide in order to have CircuitPython up and running on your Raspberry Pico. When it's installed correctly after plugin it in you should be able to see an additional drive named CIRCUIT_PYTHON or similar. At this point you can just copy paste the content of ***src*** directory onto the newly installed drive. This will cause rPico to reboot and keyboard firmware should be running. 


### *3D Printing*
Print the pieces in any color that you like, but best if:
* Bottom is non shine through color (only the glow insert is meant to pass the light)
* Glow insert is transparent filament
* Top plate is also non shine through (if you opt for a white or similar color then you'll have to cover the bottom side with tape/paint to prevent the light from shinning through)

**Top plate:**

* Infill 100%
* Layer height 0.2
* Print facing down to get a nice smooth surface (especially if you're printing on a mirror)

**Bottom:**

* Infill 30%
* Layer height 0.1
* Support **ON**

**Glow insert:**

* Infill 100%
* Layer height 0.1

![](/img/bottomprinted1.jpg)

Printed bottom part should look like this. Use a sharp tool to remove supports from USB port and glow insert slot. Use glue/hot glue to fix the the glow insert in place.

![](/img/bottomprinted2.jpg)

Use soldering iron and push in the heat inserts into designated spots. 

At this point you can also try attaching top plate. It should clip in. Check if all holes align etc.

![](/img/bottomprinted3.jpg)

### *Wiring*
Start with connecting USB-C extension.
![](/img/usb.png)

Connection diagram:
|rPico                                       |USB-C|
|:---:                                       |:---:|
|VBUS                                        |V+|
|TP2                                         |D-|
|TP3                                         |D+|
|TP1                                         |GND|

Check if wiring is correct by plugging in the rPico and checking if the internal drive has showed up. If it's OK then screw in the MCU into the bottom part of the macropad with M2/5mm screws and insert the USB-C socket into the hole at the back. Secure it with hot glue.

Insert switches, encoders into the top plate. Secure the encoders with washers and screws that came with it. Here I have used my own amoebas but you will be fine with just bare switches.

![](/img/switchesencoders.jpg)

Follow the diagrams below for wiring the matrix columns.

![](/img/matrixcols.png)

And matrix rows.

![](/img/matrixrows.png)

This is how it looked like in my case.
![](/img/rows1.jpg)
![](/img/matrixenc.png)

Now is a good time to attach the IPS screen to the top plate. Follow the below diagram in order to connect the IPS with rPico (Dotted wire is white). 
![](/img/ipscon.png)

Once this is done it's time to test it and align it properly. After booting the keyboard it should display visual help for the first layer (I've used a different image, just a white rectangle to mark the edges of the screen, but now when firmware is all done you can use default 1st layer visual guide).

![](/img/ips2.jpg) 

Align the display part of the screen with the slot and secure it with hot glue from he bottom. (Don't mind the diffrent colors on the photo it was a temporary connector back then).

![](/img/ips1.jpg)

With that out of the way we can proceed and connect our matrix with the MCU. Follow the below table and diagrams posted above for proper wiring.
### **Columns**

|Matrix                                      |MCU|
|:---                                        |:---:|
|COL_0 Red                                   |GP15|
|COL_1 Green                                 |GP14|
|COL_2 Yellow                                |GP13|
|COL_3 Black                                 |GP12|
|COL_4 White                                 |GP11|

### **Rows**
|Matrix                                      |MCU|
|:---                                        |:---:|
|Row_0 Red                                   |GP16|
|Row_1 Green                                 |GP17|
|Row_2 Black                                 |GP18|
|Row_3 White                                 |GP19|

Last thing that is left are encoders. Clip the mounting legs on the sides, we won't be needing them (thick ones). Connect 'C' pads (the one in the middle of the side with three legs) to any GND on the MCU. Then connect pads A and B from each encoder according to this table.

|Row_1 Green Encoder                         |MCU|
|:---                                        |:---:|
|Pad A                                       |GP1|
|Pad B                                       |GP0|


|Row_2 Black Encoder                         |MCU|
|:---                                        |:---:|
|Pad A                                       |GP2|
|Pad B                                       |GP3|

And last but not least RGB. Cut the amount of diodes that suits you best. I would recommend anything between 7 to 9 or 11. Wiring is quite simple. Use the GND near the data pin on the MCU.

|RGB                                         |MCU|
|:---                                        |:---:|
|VCC                                         |VBUS|
|Data                                        |GP28|
|GND                                         |GND(AGND)|

And that's it. If all went well your MacroPact should be functional. Connect it and check. If it's all good secure remaining parts with hot glue (ie. encoders, LED strip). Attach the top plate to the bottom part and screw it in with the 8mm screws. Put on the keycaps and enjoy!

You can customize the layout anyway you want. You might want to check [KMK Manual](https://github.com/KMKfw/kmk_firmware/tree/master/docs) before you do. Check **'SVG'** folder for a template for visual guide that is displayed per layer. You can use [**Inkscape**](https://inkscape.org/) for editing it and then export to PNG. In order to save space you can convert exported PNG files to low color BMP. Also note that the final picture has to be rotated 90 deg CCW.

You can edit the text for key/modifier(bottom left of each cell). Some modifiers are not visible because the stroke/fill is set to the background color. Change the color if you want the modifier to be visible. Use Unicode characters for the icons, there's plenty to choose from.

![](/img/inkscape.png)

As a last step I recommend using rubber feet to prevent the macropad from sliding on the desk. Also a magnetic USB-C cable can come handy as it won't put this much stress on the socket and is very neat.

## And this is it, hope this guide is detailed enough. Enjoy your MacroPact and please share your build on [r/MK](https://www.reddit.com/r/MechanicalKeyboards)!












