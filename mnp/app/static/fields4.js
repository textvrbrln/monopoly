
		var scene =     new THREE.Scene();
		var camera =    new THREE.PerspectiveCamera( 10, window.innerWidth / window.innerHeight, 1, 1000 );
		var renderer =  new THREE.WebGLRenderer({});

		renderer.setClearColor( 0x2ECCFA, 1)
		renderer.setSize( window.innerWidth, window.innerHeight );
		document.body.appendChild( renderer.domElement );

// Load Objects
        var objectLoader = new THREE.ObjectLoader();
        objectLoader.load("box.json", function ( obj ) {
        scene.add( obj );
    } );

// Camera
        camera.position.set(50, 50, 50);
        camera.lookAt(scene.position);
        
        var light =     new THREE.PointLight(0xffffff, 6, 40);
            light.position.set(10, 20, 15);
            scene.add(light);
		
        function render() {
			requestAnimationFrame( render );
			renderer.render( scene, camera );
		}

		render();
