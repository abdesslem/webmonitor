package Payments::Controller::Plans;
use Mojo::Base 'Mojolicious::Controller';

# This action will render a list of availables plans
sub getAll {

  my $c = shift;
  require LWP::UserAgent;
  my $ua = LWP::UserAgent->new;
  my $req = HTTP::Request->new(GET => 'https://api.stripe.com/v1/plans?limit=4');
  $req->authorization_basic('sk_test_OkmvhmRZyPAUmYtjkrKbonka', '');

  $c->render(json => $ua->request($req)->content);

}

# This action will get a single plan by id
sub get {

  my $c = shift;
  require LWP::UserAgent;
  my $ua = LWP::UserAgent->new;
  my $req = HTTP::Request->new(GET => 'https://api.stripe.com/v1/plans?limit=4');
  $req->authorization_basic('sk_test_OkmvhmRZyPAUmYtjkrKbonka', '');

  $c->render(json => $ua->request($req)->content);

}

1;
