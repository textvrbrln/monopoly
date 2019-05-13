
    var scene =     new THREE.Scene();
                    //(Field of view, Aspect Ratio, nahe sichtbare Ebene, ferne sichtb...)
    var camera =    new THREE.PerspectiveCamera(50, window.innerWidth / window.innerHeight, 1, 1000 ); 
    var renderer =  new THREE.WebGLRenderer({});

//set background color
    renderer.setClearColor( 0xFFFFFF, 1)

// viewable area in browser window
    renderer.setSize( window.innerWidth, window.innerHeight );
    document.body.appendChild( renderer.domElement );

// define field dimension
function addFieldDim (pwidth, pheight, pdepth) {
        var geometry =  new THREE.BoxGeometry(pwidth, pheight, pdepth);
        return geometry;
}

// define field material
function addFieldBasicMaterial (col) {
        var material =  new THREE.MeshBasicMaterial({
        color: col, //0x5ECD00,
        });
        return material;
}

        var plane =  new THREE.Mesh(addFieldDim(20,20,20), addFieldBasicMaterial(0x5ECD00));
        scene.add( plane );
        plane.position.set(0,0,0);
        scene.add(new THREE.AmbientLight(0x00FFC6));


// Camera
        camera.position.set(50, 50, 50);
        camera.lookAt(scene.position);
        
        var light = new THREE.PointLight(0xffffff, 6, 40);
        light.position.set(10, 20, 15);
        scene.add(light);
		
        function render() {
            
            requestAnimationFrame( render );
            renderer.render( scene, camera );
		}

		render();


            /*
            // Random number between 0.1 and 1.0
            function makerndx () {
                var rndx = Math.floor((Math.random() * 1) + 0.1);
                return rndx;
            }
            
            function makerndz () {
                var rndz = Math.floor((Math.random() * 1) + 0.1);
                return rndz;
            }
            
            function forward () {
                tile.position.x += makerndx();
                trace.position.x += makerndx();
                tile.position.z += makerndz();
                trace.position.z += makerndz();
            }
            
            if ((tile.position.x < 20 && tile.position.z < 20) || (trace.position.x < 20 && trace.position.z < 20)) {
                forward();
            }
            */
            
