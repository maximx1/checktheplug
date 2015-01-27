<!DOCTYPE html>
<html>
  <head>
    <title></title>
    <link href="http://netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css" rel="stylesheet" media="screen">
    <style>
      body {
        padding: 60px 0px;
      }
    </style>
  </head>
  <body>
    <div class="container">
      <h1>Check The Plug. Successfully signed in.</h1>
      <form role="form" method="post" action="/login">
        <table>
          <tr>
            <td class="col-md-2">
              Username:
            </td>
            <td class="col-md-2">
              <input type="text" name="username" />
            </td>
          </tr>
          <tr>
            <td class="col-md-2">
              Password:
            </td>
            <td class="col-md-2">
              <input type="password" name="password" />
            </td>
          </tr>
        </table>
        <button type="submit" class="btn btn-default">Submit</button>
      </form>
    </div>
    <script src="http://code.jquery.com/jquery-1.10.2.min.js"></script>
    <script src="http://netdna.bootstrapcdn.com/bootstrap/3.0.0/js/bootstrap.min.js"></script>
  </body>
</html>