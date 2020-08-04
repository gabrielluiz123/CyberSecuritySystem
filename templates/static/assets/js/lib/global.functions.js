global.auth = false;
global.onRequest = false;
global.isAuthenticated = function()
{
    $.post('api/usr/login', {
        execution: 'is_logged_in'
    }, function(r){
        regAuth(r)
    }, 'json')
}

function regAuth(r)
{
    auth = r.res;
}
global.requestRelease = function(){
    setTimeout(function(){
        onRequest = false;
    }, 300)
}

global.resizeImage = function(img, maxWidth, maxHeight)
{
  return new Promise((resolve, reject) => {
    let image = new Image();
    image.src = URL.createObjectURL(img);
    image.onload = () => {
      let width = image.width;
      let height= image.height;

      if(width <= maxWidth && height <= maxHeight){
        resolve(img);
      }

      let newWidth;
      let newHeight;

      if(width > height){
        newHeight = height * (maxWidth / width);
        newWidth  = maxWidth;
      }else{
        newWidth = width * (maxHeight/height);
        newHeight= maxHeight;
      }

    let canvas = document.createElement('canvas');
    canvas.width = newWidth;
    canvas.height= newHeight;

    let ctx = canvas.getContext('2d');

    ctx.drawImage(image, 0, 0, newWidth, newHeight);

    canvas.toBlob(resolve, img.type)

    };
    img.onerror = reject;
  })
}