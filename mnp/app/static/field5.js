
		var scene =     new THREE.Scene();
		var camera =    new THREE.PerspectiveCamera( 10, window.innerWidth / window.innerHeight, 1, 1000 );
		var renderer =  new THREE.WebGLRenderer({});

		renderer.setClearColor( 0xffffff, 1)
		renderer.setSize( window.innerWidth, window.innerHeight );
		document.body.appendChild( renderer.domElement );

// Box 1
class newtile (vx,vy,vz){
        var geometry =  new THREE.BoxGeometry( 1, 0.1, 1 );
        var material =  new THREE.MeshPhongMaterial({
        ambient: 0x555555,
        color: 0x555555,
        specular: 0xffffff,
        shininess: 50,
        shading: THREE.SmoothShading
});
        var tile1 =      new THREE.Mesh(geometry, material);
        tile1.position.x = vx;
        tile1.position.y = vy;
        tile1.position.z = vz;
        scene.add( tile1 );
        scene.add(new THREE.AmbientLight(0x4000ff));
}


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
