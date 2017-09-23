package Payments::Controller::Plans;
use Mojo::Base 'Mojolicious::Controller';
use LWP::UserAgent;

my $planUrl = 'https://api.stripe.com/v1/plans';
# This action will render a list of availables plans
sub getAll {

  my $c = shift;
  my $ua = LWP::UserAgent->new;
  my $req = HTTP::Request->new(GET => $planUrl);
  $req->authorization_basic('sk_test_OkmvhmRZyPAUmYtjkrKbonka', '');

  $c->render(json => $ua->request($req)->content);

}

# This action will get a single plan by id
sub get {

  my $c = shift;
  my $ua = LWP::UserAgent->new;
  my $req = HTTP::Request->new(GET => $planUrl);
  $req->authorization_basic('sk_test_OkmvhmRZyPAUmYtjkrKbonka', '');

  $c->render(json => $ua->request($req)->content);

}
1;
