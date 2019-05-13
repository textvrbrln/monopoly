
		var scene =     new THREE.Scene();
		var camera =    new THREE.PerspectiveCamera( 10, window.innerWidth / window.innerHeight, 1, 1000 );
		var renderer =  new THREE.WebGLRenderer({});

		renderer.setClearColor( 0xffffff, 1)
		renderer.setSize( window.innerWidth, window.innerHeight );
		document.body.appendChild( renderer.domElement );

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

// Camera
        camera.position.set(20, 20, 20);
        camera.lookAt(scene.position);
        
        var light =     new THREE.PointLight(0xffffff, 6, 40);
        light.position.set(10, 20, 15);
        scene.add(light);
		
        function render() {
			requestAnimationFrame( render );
			renderer.render( scene, camera );
		}

		render();
