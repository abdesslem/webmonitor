package Payments;
use Mojo::Base 'Mojolicious';

# This method will run once at server start
sub startup {
  my $self = shift;

  # Documentation browser under "/perldoc"
  $self->plugin('PODRenderer');

  # Router
  my $r = $self->routes;

  # Normal route to controller
  $r->get('/')->to(controller => 'Plans', action => 'getAll');
  $r->get('/plans')->to(controller => 'Plans', action => 'get');
  #s$r->post('/plans')->to(controller => 'plans', action => 'post');

  # Normal route to controller
  $r->post('/checkout')->to(controller => 'checkout', action => 'post');

}

1;
