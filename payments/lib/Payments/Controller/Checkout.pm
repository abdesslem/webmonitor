package Payments::Controller::Checkout;
use Mojo::Base 'Mojolicious::Controller';
use LWP::UserAgent;


# 1 the client have to connect => get the email
# 2 check if the customer registred, if not register customer
# 3 subscribe

# This action will render a template
sub post {

  my $self = shift;

  my $ua = LWP::UserAgent->new;

  # check the customer in a local database
  # Get or create a new customer
  my $req = HTTP::Request->new(POST => 'https://api.stripe.com/v1/customers');
  $req->content('email=amriabdesslem@gmail.com');
  $req->authorization_basic('sk_test_OkmvhmRZyPAUmYtjkrKbonka', '');
  my $res = $ua->request($req);
  # Check the outcome of the response
  if ($res->is_success) {
      # Save the customer info in the local database
      print Data::Dumper::Dumper($res->content);
      # subscriptions of customer
      $req = HTTP::Request->new(POST => 'https://api.stripe.com/v1/subscriptions');
      $req->content('customer=customerid&plan=planid');
      $req->authorization_basic('sk_test_OkmvhmRZyPAUmYtjkrKbonka', '');
      $res = $ua->request($req);
  }
  # Render template "example/welcome.html.ep" with message
  $self->render(text => 'I ♥ Mojolicious!');
}

1;
