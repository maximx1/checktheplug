<!DOCTYPE html>
<html>
	<head>
		<title>{{title}}</title>
		<script type="application/javascript" src="https://code.jquery.com/jquery-2.1.0.min.js"></script>
        <link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/foundation/5.5.0/css/foundation.min.css">
	</head>
	<body>
		<div id="mainContainer">
			<div class="contain-to-grid header-section">
			    <nav class="top-bar" data-topbar>
					<ul class="title-area">
						<li class="name">
							<h1><a href="#">Check the Plug</a></h1>
						</li>
						<li class="toggle-topbar menu-icon"><a href="#"><span></span></a></li>
				  	</ul>
					
					<div class="section top-bar-section">
						<ul class="right">
							<li class="active"><a href="/">Home</a></li>
							<li><a href="#">Api</a></li>
							<li class="has-dropdown">
								<a href="#">Applications</a>
								<ul class="dropdown">
									<li><a href="/search">Look Up</a></li>
									<li><a href="/create">Create New</a></li>
								</ul>
							</li>
							<li><a href="/logout">Log Out</a></li>
						</ul>
					</div>
				</nav>
			</div>
			<div class="header-fill"></div>
			<div class="row">Search:</div>
            <div class="row">
                <div class="columns small-12 medium-12 large-4 large-centered"><input type="text" name="searchterm" placeholder="Search Applications" autofocus value='{{ searchTerm if searchTerm else "" }}' /></div>
            </div>
            <div class="row">
                <div class="columns small-12 medium-12 large-4 large-centered"><button type="submit" class="button expand radius">Search By Name</button></div>
            </div>
		</div>
        <script type="application/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/foundation/5.5.0/js/foundation.min.js"></script>
		<script>
			$(document).foundation();
		</script>
	</body>
</html>