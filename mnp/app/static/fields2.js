
    var scene =     new THREE.Scene();
                    //(Field of view, Aspect Ratio, nahe sichtbare Ebene, ferne sichtb...)
    var camera =    new THREE.PerspectiveCamera(50, window.innerWidth / window.innerHeight, 1, 1000 ); 
    var renderer =  new THREE.WebGLRenderer({});

    //set background color
    renderer.setClearColor( 0xFFFFFF, 1)
    // viewable area in browser window
    renderer.setSize( window.innerWidth, window.innerHeight );
    document.body.appendChild( renderer.domElement );

// Plane
        // Tile dimensions
        var plane_width = 50;
        var plane_height = 50;
        var plane_depth = 0;
        
        // Plane Position
        var globalPosX = 0;
        var globalPosY = 0;
        var globalPosZ = 0;

        var geometry =  new THREE.BoxGeometry( plane_width, plane_depth, plane_height );
        var material =  new THREE.MeshBasicMaterial({
        ambient: 0xFFFFFF,
        color: 0x5ECD00,
        specular: 0xffffff,
        shininess: 50,
        shading: THREE.SmoothShading
});
        var plane =  new THREE.Mesh(geometry, material);
        plane.position.x = globalPosX;
        plane.position.y = globalPosY;
        plane.position.z = globalPosZ;
        scene.add( plane );
        scene.add(new THREE.AmbientLight(0x00FFC6));

// Unit positions
        // Box dimensions
        var width = 5;
        var height = 5;
        var depth = 5;
        
        // Absolute Position
        var globalPosX = -20;
        var globalPosY = 5;
        var globalPosZ = -20;
        
// Unit 
        var geometry =  new THREE.BoxGeometry( width, depth, height );
        var material =  new THREE.MeshPhongMaterial({
        //var material =  new THREE.MeshBasicMaterial({
        ambient: 0xFFFFFF,
        color: 0x20C220,
        specular: 0xffffff,
        shininess: 50,
        shading: THREE.SmoothShading
});
        var tile =  new THREE.Mesh(geometry, material);
        tile.position.x = globalPosX;
        tile.position.y = globalPosY;
        tile.position.z = globalPosZ;
        scene.add( tile );
        scene.add(new THREE.AmbientLight(0x00FFC6));

// Trace
        var geometry =  new THREE.BoxGeometry( width, depth, height );
        var material =  new THREE.MeshPhongMaterial({
        //var material =  new THREE.MeshBasicMaterial({
        ambient: 0xFFFFFF,
        color: 0x000000,
        specular: 0xffffff,
        shininess: 50,
        shading: THREE.SmoothShading
});
        var trace =  new THREE.Mesh(geometry, material);
        trace.position.x = globalPosX;
        trace.position.y = globalPosY;
        trace.position.z = globalPosZ;
        scene.add( trace );
        scene.add(new THREE.AmbientLight(0x00FFC6));
        

// Camera
        camera.position.set(50, 50, 50);
        camera.lookAt(scene.position);
        
        var light = new THREE.PointLight(0xffffff, 6, 40);
        light.position.set(10, 20, 15);
        scene.add(light);
		
        function render() {
            
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
            
            requestAnimationFrame( render );
            renderer.render( scene, camera );
		}

		render();


/*
// Box 1
        var geometry =  new THREE.BoxGeometry( 1, 0.1, 1 );
        var material =  new THREE.MeshPhongMaterial({
        ambient: 0x555555,
        color: 0x555555,
        specular: 0xffffff,
        shininess: 50,
        shading: THREE.SmoothShading
});
        var tile1 =      new THREE.Mesh(geometry, material);
        tile1.position.x = -5;
        tile1.position.y = -5;
        tile1.position.z = 0;
        scene.add( tile1 );
        scene.add(new THREE.AmbientLight(0x4000ff));

// Box 2
        var geometry =  new THREE.BoxGeometry( 0.95, 0.1, 0.95 );
        var material =  new THREE.MeshPhongMaterial({
        ambient: 0x555555,
        color: 0x555555,
        specular: 0xffffff,
        shininess: 50,
        shading: THREE.SmoothShading
});
        var tile2 =      new THREE.Mesh(geometry, material);
        tile2.position.x = -3.6;
        tile2.position.y = -3.6;
        tile2.position.z = 0;
        scene.add( tile2 );
        scene.add(new THREE.AmbientLight(0x4000ff));


// Box 3
        var geometry =  new THREE.BoxGeometry( 0.9, 0.1, 0.9 );
        var material =  new THREE.MeshPhongMaterial({
        ambient: 0x555555,
        color: 0x555555,
        specular: 0xffffff,
        shininess: 50,
        shading: THREE.SmoothShading
});
        var tile3 =      new THREE.Mesh(geometry, material);
        tile3.position.x = -2.35;
        tile3.position.y = -2.35;
        tile3.position.z = 0;
        scene.add( tile3 );
        scene.add(new THREE.AmbientLight(0x4000ff));

// Box 4
        var geometry =  new THREE.BoxGeometry( 0.85, 0.1, 0.85 );
        var material =  new THREE.MeshPhongMaterial({
        ambient: 0x555555,
        color: 0x555555,
        specular: 0xffffff,
        shininess: 50,
        shading: THREE.SmoothShading
});
        var tile3 =      new THREE.Mesh(geometry, material);
        tile3.position.x = -1.2;
        tile3.position.y = -1.2;
        tile3.position.z = 0;
        scene.add( tile3 );
        scene.add(new THREE.AmbientLight(0x4000ff));
*/

