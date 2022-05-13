IMAGEPATH = "https://dl.dropboxusercontent.com/1/view/mrskfxn7v4fqggg/CITS3403Project/image2.jpg";
// IMAGEPATH = "image2.jpg"

/**
 * 80% Done
 * Tasks:
 *  Find a way to use original file to update canvas and not
 *  Current Canvas to pixellate image
 *  Pixeltate the Image on Window Load (Do FIRST)
 */


//As we decrement the pixel size you have to use the og file to update the canvas
// Not accessing the pixelated image now.

const canvas = document.getElementById("canvas1");
const btn = document.getElementById("btn");
const ctx = canvas.getContext('2d');



const incrementBtn = document.getElementById("increment");
//pixel value
const pixelValue = document.getElementById("number");
var count = 20;
pixelValue.innerHTML = count;


canvas.width = 900;
canvas.height = 900;

const image1 = new Image();
image1.src = IMAGEPATH;
image1.crossOrigin="anonymous";



//Keep OrignalImag locally for Repixelation
// const ctxOrigin = getContext('2d');
// const OriginalImage = new Image();
// OriginalImage.src = IMAGEPATH;
// OriginalImage.crossOrigin="anonymous";
// ctx = ctxOrigin; //Testing Codes


//After the image has been loaded run draw image
image1.addEventListener('load', function(){
    console.log("image loaded");
    // ctx.drawImage(image1, 0, 0);
    ctx.drawImage(image1, 0, 0, canvas.width, canvas.height);
    // ctxOrigin.drawImage(image1, 0, 0, canvas.width, canvas.height);
});


incrementBtn.addEventListener('click', function(){
    count = count - 2;
    pixelValue.innterHTML = count;
    //Update Pixel counter
});

//Can you reference a ctx into another ctx??

ctx.addEventListener('ready', function(){
    //Run Pixellation Function
    console.log("load");
    let pixelArr = ctx.getImageData(0,0, canvas.width,canvas.height).data;
    // let sample_size = count; //Larger Sample Larger Squaresize
    let sample_size = 10;
    ctx.clearRect(0,0,canvas.width,canvas.height);
    for(let y=0;y<canvas.height;y+=sample_size)
        for(let x=0;x<canvas.width;x+=sample_size){
            let p = (x+(y*canvas.width))*4;
            ctx.fillStyle = "rgba(" + 
            pixelArr[p] + "," +
            pixelArr[p+1] + "," +
            pixelArr[p+2] + "," +
            pixelArr[p+3] + ")";

            ctx.fillRect(x,y,sample_size,sample_size);
        };
});