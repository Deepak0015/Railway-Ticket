
        function check(){
            var v1=document.getElementById("place1")
            var v2=document.getElementById("place2")
            var p0=document.getElementById("fack")
            var p1=document.getElementById("chennai-tirunelveli")
            var p2=document.getElementById("tirunelveli-chennai")
            var p3=document.getElementById("chennai-coimbutore")
            var p4=document.getElementById("coimbutore-chennai")
            var p5=document.getElementById("chennai-delhi")
            var p6=document.getElementById("delhi-chennai")
            var p7=document.getElementById("chennai-mumbai")
            var p8=document.getElementById("mumbai-chennai")
            var p9=document.getElementById("tirunelveli-coimbutore")
            var p10=document.getElementById("tirunelveli-mumbai")
            var p11=document.getElementById("tirunelveli-delhi")
            var p12=document.getElementById("coimbutore-delhi")
            var p13=document.getElementById("coimbutore-mumbai")
            var p14=document.getElementById("coimbutore-tirunelveli")
            var p15=document.getElementById("mumbai-delhi")
            var p16=document.getElementById("mumbai-coimbutore")
            var p17=document.getElementById("mumbai-tirunelveli")
            var p18=document.getElementById("delhi-mumbai")
            var p19=document.getElementById("delhi-coimbutore")
            var p20=document.getElementById("delhi-tirunelveli")
            var amounts=document.getElementById("amounts")
            var amdiv=document.getElementById("amdiv")
            var starttime=document.getElementById("starttime")
            if(v1. value==="no" || v2.value==="no"){
                alert("Please Enter Start and Destination place...")
            }
            if(v1.value==v2.value && (v1.value!="no" || v2.value!="no")){
                alert("There is no Direct Train between the station...")
            }
            if(v1.value==="chennai" && v2.value==="tirunelveli" && v1.value!=v2.value){
                amdiv.textContent='₹ 215'
                amounts.value="215"
                p0.style.display="none"
                p1.style.display="inline-block"
                starttime.value=p1.value
                p2.style.display="none"
                p3.style.display="none"
                p4.style.display="none"
                p5.style.display="none"
                p6.style.display="none"
                p7.style.display="none"
                p8.style.display="none"
                p9.style.display="none"
                p10.style.display="none"
                p11.style.display="none"
                p12.style.display="none"
                p13.style.display="none"
                p14.style.display="none"
                p15.style.display="none"
                p16.style.display="none"
                p17.style.display="none"
                p18.style.display="none"
                p19.style.display="none"
                p20.style.display="none"
                console.log(starttime)
                console.log(amounts)
            }
            if(v1.value==="tirunelveli" && v2.value==="chennai" && v1.value!=v2.value){
                amdiv.textContent='₹ 215'
                amounts.value='215'
                p0.style.display="none"
                p2.style.display="inline-block"
                starttime.value=p2.value
                p1.style.display="none"
                p3.style.display="none"
                p4.style.display="none"
                p5.style.display="none"
                p6.style.display="none"
                p7.style.display="none"
                p8.style.display="none"
                p9.style.display="none"
                p10.style.display="none"
                p11.style.display="none"
                p12.style.display="none"
                p13.style.display="none"
                p14.style.display="none"
                p15.style.display="none"
                p16.style.display="none"
                p17.style.display="none"
                p18.style.display="none"
                p19.style.display="none"
                p20.style.display="none"
            
            }
            if(v1.value==="chennai" && v2.value==="coimbutore" && v1.value!=v2.value){
                amdiv.textContent='₹ 190'
                p0.style.display="none"
                p3.style.display="inline-block"
                starttime.value=p3.value
                p1.style.display="none"
                p2.style.display="none"
                p4.style.display="none"
                p5.style.display="none"
                p6.style.display="none"
                p7.style.display="none"
                p8.style.display="none"
                p9.style.display="none"
                p10.style.display="none"
                p11.style.display="none"
                p12.style.display="none"
                p13.style.display="none"
                p14.style.display="none"
                p15.style.display="none"
                p16.style.display="none"
                p17.style.display="none"
                p18.style.display="none"
                p19.style.display="none"
                p20.style.display="none"
            
            }
            if(v1.value==="coimbutore" && v2.value==="chennai" && v1.value!=v2.value){
                amdiv.textContent='₹ 190'
                p0.style.display="none"
                p4.style.display="inline-block"
                starttime.value=p4.value
                p1.style.display="none"
                p2.style.display="none"
                p3.style.display="none"
                p5.style.display="none"
                p6.style.display="none"
                p7.style.display="none"
                p8.style.display="none"
                p9.style.display="none"
                p10.style.display="none"
                p11.style.display="none"
                p12.style.display="none"
                p13.style.display="none"
                p14.style.display="none"
                p15.style.display="none"
                p16.style.display="none"
                p17.style.display="none"
                p18.style.display="none"
                p19.style.display="none"
                p20.style.display="none"
            
            }
            if(v1.value==="delhi" && v2.value==="chennai" && v1.value!=v2.value){
                amdiv.textContent='₹ 505'
                p0.style.display="none"
                p6.style.display="inline-block"
                starttime.value=p6.value
                p1.style.display="none"
                p2.style.display="none"
                p3.style.display="none"
                p4.style.display="none"
                p5.style.display="none"
                p7.style.display="none"
                p8.style.display="none"
                p9.style.display="none"
                p10.style.display="none"
                p11.style.display="none"
                p12.style.display="none"
                p13.style.display="none"
                p14.style.display="none"
                p15.style.display="none"
                p16.style.display="none"
                p17.style.display="none"
                p18.style.display="none"
                p19.style.display="none"
                p20.style.display="none"
            
            }
            if(v1.value==="chennai" && v2.value==="delhi" && v1.value!=v2.value){
                amdiv.textContent='₹ 505'
                p0.style.display="none"
                p5.style.display="inline-block"
                starttime.value=p5.value
                p1.style.display="none"
                p2.style.display="none"
                p3.style.display="none"
                p4.style.display="none"
                p6.style.display="none"
                p7.style.display="none"
                p8.style.display="none"
                p9.style.display="none"
                p10.style.display="none"
                p11.style.display="none"
                p12.style.display="none"
                p13.style.display="none"
                p14.style.display="none"
                p15.style.display="none"
                p16.style.display="none"
                p17.style.display="none"
                p18.style.display="none"
                p19.style.display="none"
                p20.style.display="none"
            
            }
            if(v1.value==="chennai" && v2.value==="mumbai" && v1.value!=v2.value){
                amdiv.textContent='₹ 360'
                p0.style.display="none"
                p7.style.display="inline-block"
                starttime.value=p7.value
                p1.style.display="none"
                p2.style.display="none"
                p3.style.display="none"
                p4.style.display="none"
                p5.style.display="none"
                p6.style.display="none"
                p8.style.display="none"
                p9.style.display="none"
                p10.style.display="none"
                p11.style.display="none"
                p12.style.display="none"
                p13.style.display="none"
                p14.style.display="none"
                p15.style.display="none"
                p16.style.display="none"
                p17.style.display="none"
                p18.style.display="none"
                p19.style.display="none"
                p20.style.display="none"
            
            }
            if(v1.value==="mumbai" && v2.value==="chennai" && v1.value!=v2.value){
                amdiv.textContent='₹ 360'
                p0.style.display="none"
                p8.style.display="inline-block"
                starttime.value=p8.value
                p1.style.display="none"
                p2.style.display="none"
                p3.style.display="none"
                p4.style.display="none"
                p5.style.display="none"
                p6.style.display="none"
                p7.style.display="none"
                p9.style.display="none"
                p10.style.display="none"
                p11.style.display="none"
                p12.style.display="none"
                p13.style.display="none"
                p14.style.display="none"
                p15.style.display="none"
                p16.style.display="none"
                p17.style.display="none"
                p18.style.display="none"
                p19.style.display="none"
                p20.style.display="none"
            
            }
            if(v1.value==="tirunelveli" && v2.value==="coimbutore" && v1.value!=v2.value){
                amdiv.textContent='₹ 210'
                p0.style.display="none"
                p9.style.display="inline-block"
                starttime.value=p9.value
                p1.style.display="none"
                p2.style.display="none"
                p3.style.display="none"
                p4.style.display="none"
                p5.style.display="none"
                p6.style.display="none"
                p7.style.display="none"
                p8.style.display="none"
                p10.style.display="none"
                p11.style.display="none"
                p12.style.display="none"
                p13.style.display="none"
                p14.style.display="none"
                p15.style.display="none"
                p16.style.display="none"
                p17.style.display="none"
                p18.style.display="none"
                p19.style.display="none"
                p20.style.display="none"
            }
            if(v1.value==="tirunelveli" && v2.value==="mumbai" && v1.value!=v2.value){
                amdiv.textContent='₹ 450'
                p10.style.display="inline-block"
                starttime.value=p10.value
                p0.style.display="none"
                p1.style.display="none"
                p2.style.display="none"
                p3.style.display="none"
                p4.style.display="none"
                p5.style.display="none"
                p6.style.display="none"
                p7.style.display="none"
                p8.style.display="none"
                p9.style.display="none"
                p11.style.display="none"
                p12.style.display="none"
                p13.style.display="none"
                p14.style.display="none"
                p15.style.display="none"
                p16.style.display="none"
                p17.style.display="none"
                p18.style.display="none"
                p19.style.display="none"
                p20.style.display="none"

            }
            if(v1.value==="tirunelveli" && v2.value==="delhi" && v1.value!=v2.value){
                amdiv.textContent='₹ 585'
                p11.style.display="inline-block"
                starttime.value=p11.value
                p0.style.display="none"
                p1.style.display="none"
                p2.style.display="none"
                p3.style.display="none"
                p4.style.display="none"
                p5.style.display="none"
                p6.style.display="none"
                p7.style.display="none"
                p8.style.display="none"
                p9.style.display="none"
                p10.style.display="none"
                p12.style.display="none"
                p13.style.display="none"
                p14.style.display="none"
                p15.style.display="none"
                p16.style.display="none"
                p17.style.display="none"
                p18.style.display="none"
                p19.style.display="none"
                p20.style.display="none"

            }
            if(v1.value==="coimbutore" && v2.value==="delhi" && v1.value!=v2.value){
                amdiv.textContent='₹ 560'
                p12.style.display="inline-block"
                starttime.value=p12.value
                p0.style.display="none"
                p1.style.display="none"
                p2.style.display="none"
                p3.style.display="none"
                p4.style.display="none"
                p5.style.display="none"
                p6.style.display="none"
                p7.style.display="none"
                p8.style.display="none"
                p9.style.display="none"
                p10.style.display="none"
                p11.style.display="none"
                p13.style.display="none"
                p14.style.display="none"
                p15.style.display="none"
                p16.style.display="none"
                p17.style.display="none"
                p18.style.display="none"
                p19.style.display="none"
                p20.style.display="none"
            }
            if(v1.value==="coimbutore" && v2.value==="mumbai" && v1.value!=v2.value){
                amdiv.textContent='₹ 380'
                p13.style.display="inline-block"
                starttime.value=p13.value
                p0.style.display="none"
                p1.style.display="none"
                p2.style.display="none"
                p3.style.display="none"
                p4.style.display="none"
                p5.style.display="none"
                p6.style.display="none"
                p7.style.display="none"
                p8.style.display="none"
                p9.style.display="none"
                p10.style.display="none"
                p11.style.display="none"
                p12.style.display="none"
                p14.style.display="none"
                p15.style.display="none"
                p16.style.display="none"
                p17.style.display="none"
                p18.style.display="none"
                p19.style.display="none"
                p20.style.display="none"
            }
            if(v1.value==="coimbutore" && v2.value==="tirunelveli" && v1.value!=v2.value){
                amdiv.textContent='₹ 180'
                p14.style.display="inline-block"
                starttime.value=p14.value
                p0.style.display="none"
                p1.style.display="none"
                p2.style.display="none"
                p3.style.display="none"
                p4.style.display="none"
                p5.style.display="none"
                p6.style.display="none"
                p7.style.display="none"
                p8.style.display="none"
                p9.style.display="none"
                p10.style.display="none"
                p11.style.display="none"
                p12.style.display="none"
                p13.style.display="none"
                p15.style.display="none"
                p16.style.display="none"
                p17.style.display="none"
                p18.style.display="none"
                p19.style.display="none"
                p20.style.display="none"
            }
            if(v1.value==="mumbai" && v2.value==="delhi" && v1.value!=v2.value){
                amdiv.textContent='₹ 400'
                p15.style.display="inline-block"
                starttime.value=p15.value
                p0.style.display="none"
                p1.style.display="none"
                p2.style.display="none"
                p3.style.display="none"
                p4.style.display="none"
                p5.style.display="none"
                p6.style.display="none"
                p7.style.display="none"
                p8.style.display="none"
                p9.style.display="none"
                p10.style.display="none"
                p11.style.display="none"
                p12.style.display="none"
                p13.style.display="none"
                p14.style.display="none"
                p16.style.display="none"
                p17.style.display="none"
                p18.style.display="none"
                p19.style.display="none"
                p20.style.display="none"
            }
            if(v1.value==="mumbai" && v2.value==="coimbutore" && v1.value!=v2.value){
                amdiv.textContent='₹ 375'
                p16.style.display="inline-block"
                starttime.value=p16.value
                p0.style.display="none"
                p1.style.display="none"
                p2.style.display="none"
                p3.style.display="none"
                p4.style.display="none"
                p5.style.display="none"
                p6.style.display="none"
                p7.style.display="none"
                p8.style.display="none"
                p9.style.display="none"
                p10.style.display="none"
                p11.style.display="none"
                p12.style.display="none"
                p13.style.display="none"
                p14.style.display="none"
                p15.style.display="none"
                p17.style.display="none"
                p18.style.display="none"
                p19.style.display="none"
                p20.style.display="none"
            }
            if(v1.value==="mumbai" && v2.value==="tirunelveli" && v1.value!=v2.value){
                amdiv.textContent='₹ 470'
                p17.style.display="inline-block"
                starttime.value=p17.value
                p0.style.display="none"
                p1.style.display="none"
                p2.style.display="none"
                p3.style.display="none"
                p4.style.display="none"
                p5.style.display="none"
                p6.style.display="none"
                p7.style.display="none"
                p8.style.display="none"
                p9.style.display="none"
                p10.style.display="none"
                p11.style.display="none"
                p12.style.display="none"
                p13.style.display="none"
                p14.style.display="none"
                p15.style.display="none"
                p16.style.display="none"
                p18.style.display="none"
                p19.style.display="none"
                p20.style.display="none"
            }
            if(v1.value==="delhi" && v2.value==="mumbai" && v1.value!=v2.value){
                amdiv.textContent='₹ 375'
                p18.style.display="inline-block"
                starttime.value=p18.value
                p0.style.display="none"
                p1.style.display="none"
                p2.style.display="none"
                p3.style.display="none"
                p4.style.display="none"
                p5.style.display="none"
                p6.style.display="none"
                p7.style.display="none"
                p8.style.display="none"
                p9.style.display="none"
                p10.style.display="none"
                p11.style.display="none"
                p12.style.display="none"
                p13.style.display="none"
                p14.style.display="none"
                p15.style.display="none"
                p16.style.display="none"
                p17.style.display="none"
                p19.style.display="none"
                p20.style.display="none"
            }
            if(v1.value==="delhi" && v2.value==="coimbutore" && v1.value!=v2.value){
                amdiv.textContent='₹ 560'
                p19.style.display="inline-block"
                starttime.value=p19.value
                p0.style.display="none"
                p1.style.display="none"
                p2.style.display="none"
                p3.style.display="none"
                p4.style.display="none"
                p5.style.display="none"
                p6.style.display="none"
                p7.style.display="none"
                p8.style.display="none"
                p9.style.display="none"
                p10.style.display="none"
                p11.style.display="none"
                p12.style.display="none"
                p13.style.display="none"
                p14.style.display="none"
                p15.style.display="none"
                p16.style.display="none"
                p17.style.display="none"
                p18.style.display="none"
                p20.style.display="none"


            }
            if(v1.value==="delhi" && v2.value==="tirunelveli" && v1.value!=v2.value){
                amdiv.textContent='₹ 585'
                p20.style.display="inline-block"
                starttime.value=p20.value
                p0.style.display="none"
                p1.style.display="none"
                p2.style.display="none"
                p3.style.display="none"
                p4.style.display="none"
                p5.style.display="none"
                p6.style.display="none"
                p7.style.display="none"
                p8.style.display="none"
                p9.style.display="none"
                p10.style.display="none"
                p11.style.display="none"
                p12.style.display="none"
                p13.style.display="none"
                p14.style.display="none"
                p15.style.display="none"
                p16.style.display="none"
                p17.style.display="none"
                p18.style.display="none"
                p19.style.display="none"
            }
        }

        // Retrieve the Base64 image data from localStorage
        const imageData = localStorage.getItem('capturedImage');

        // Display the image on the page
        if (imageData) {
            const myicon = document.getElementById('myicon');
            myicon.value = imageData;
            console.log(myicon.value)
            // Set the Base64 data as the src of the image
        } else {
            console.log('No image data found.');
        }