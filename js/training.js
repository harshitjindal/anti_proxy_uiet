<script type="text/javascript">
//--------------------
// GET USER MEDIA CODE
//--------------------
navigator.getUserMedia = ( navigator.getUserMedia ||
                          navigator.webkitGetUserMedia ||
                          navigator.mozGetUserMedia ||
                          navigator.msGetUserMedia);

var video;
var webcamStream;

function startWebcam() {
    if (navigator.getUserMedia) {
        navigator.getUserMedia (
                                
                                // constraints
                                {
                                video: true,
                                audio: false
                                },
                                
                                // successCallback
                                function(localMediaStream) {
                                video = document.querySelector('video');
                                video.src = window.URL.createObjectURL(localMediaStream);
                                webcamStream = localMediaStream;
                                },
                                
                                // errorCallback
                                function(err) {
                                console.log("The following error occured: " + err);
                                }
                                );
    } else {
        console.log("getUserMedia not supported");
    }
}


//---------------------
// TAKE A SNAPSHOT CODE
//---------------------
var canvas, ctx;

function init() {
    // Get the canvas and obtain a context for
    // drawing in it
    canvas = document.getElementById("myCanvas");
    ctx = canvas.getContext('2d');
}

function snapshot() {
    
    ctx.drawImage(video, 0,0, canvas.width, canvas.height);
    var img1 = new Image();
    img1.src = canvas.toDataURL();
    var ip = document.getElementById('ip').value;
    datad = "{\r\n    \"image\":\"" + img1.src+ "\",\r\n    \"subject_id\":\"" + ip + "\",\r\n    \"gallery_name\":\"Arti\"\r\n}";
    var settings = {
        "async": true,
        "crossDomain": true,
        "url": "https://api.kairos.com/enroll",
        "method": "POST",
        "headers": {
            "content-type": "application/json",
            "app_id": "63e167c7",
            "app_key": "cccf0f5ffbd82f6573d1ba8f80288e74",
            "cache-control": "no-cache"
        },
        "processData": false,
        "data": datad
    }
    
    $.ajax(settings).done(function (response) {
                          //
                          if((response.images[0].transaction.status) == "success"){
                          Materialize.toast("Image Trained succesfully by name " +response.images[0].transaction.subject_id+ " in gallery name " +response.images[0].transaction.gallery_name, 4000);
                          }
                          else{
                          Materialize.toast("Unable to Train Image", 4000);
                          }
                          });
    //console.log(img1.src);
}

</script>
</html>