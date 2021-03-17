const expected_canvas_count = 8;

$(document).ready(function(){
    var canvas_check = setInterval(checkForCanvases, 3000);

    // Callback function to execute when mutations are observed
    const callback = function(mutationsList, observer) {
        // Use traditional 'for loops' for IE 11
        for(const mutation of mutationsList) {
            if (mutation.type === 'attributes') {
                if(mutation.attributeName == 'height' || mutation.attributeName == 'width' ){
                    // console.log('The ' + mutation.attributeName + ' attribute was modified.');
                    // console.log('The mutation ' + mutation.target);
                    canvasDimensionsAdjustment(mutation.target);
                }
            }
        }
    };

    // Create an observer instance linked to the callback function
    const observer = new MutationObserver(callback);

    function canvasDimensionsAdjustment(canvas){
        if(canvas.getAttribute('width') % 1 != 0){
            // console.log('not whole number', mutation.target.getAttribute('width'));
            canvas.setAttribute('width', Math.round(canvas.getAttribute('width')));
        }
        if(canvas.getAttribute('height') % 1 != 0){
            // console.log('not whole number', mutation.target.getAttribute('heightheight'));
            canvas.setAttribute('height', Math.round(canvas.getAttribute('height')));
        }
    }

    function checkForCanvases(){
        console.log('checking for canvases');
        var canvases = $('canvas');
        if(canvases.size() > 0){
            console.log('canvases found: '+canvases.size(), canvases );
            canvasObserver(canvases);
            canvases.each(function(){
                canvasDimensionsAdjustment(this);
            });
            if(canvases.size() >= expected_canvas_count){
                clearInterval(canvas_check);
                console.log('stopped checking for canvases');
            }
            
            return true;
        }
        return false;
    }
    
    
    function canvasObserver(canvases){
        // Select the node that will be observed for mutations
        var targetNodes = canvases;
    
        // Options for the observer (which mutations to observe)
        const config = { attributes: true, childList: true, subtree: true };
    
        // Start observing the target node for configured mutations
        // observer.observe(targetNode, config);
        targetNodes.each(function(){
            observer.observe(this, config);
        });
    }
});