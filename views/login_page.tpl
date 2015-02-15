<!DOCTYPE html>
<html>
	<head>
		<title>{{title}}</title>
        <link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/foundation/5.5.0/css/foundation.min.css"
	</head>
	<body>
		<div id="mainContainer">
			<br />
			<div class="row">
				<div class="small-12 medium-8 large-8 push-2 columns text-center">
				  <h1>Check The Plug. Sign in time.</h1>
				</div>
			</div>
			<form role="form" method="post" action="/login" style="border: solid 1;padding: 1em;">
				<div class="row">
					<div class="columns small-12 medium-12 large-4 large-centered"><input type="text" name="username" placeholder="Username" autofocus /></div>
				</div>
				<div class="row">
					<div class="columns small-12 medium-12 large-4 large-centered"><input type="password" name="password" placeholder="Password" /></div>
				</div>
				<div class="row">
					<div class="columns small-12 medium-12 large-4 large-centered"><button type="submit" class="button expand radius">Log In</button></div>
				</div>
            </form>
		</div>
        <script type="application/javascript" src="https://code.jquery.com/jquery-2.1.3.min.js" />
        <script type="application/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/foundation/5.5.0/js/foundation/foundation.abide.js" />
	</body>
</html>