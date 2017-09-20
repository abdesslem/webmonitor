use Mojo::Base -strict;

use Test::More;
use Test::Mojo;

my $t = Test::Mojo->new('Payments');
$t->get_ok('/')->status_is(200)->content_like(qr/Mojolicious/i);

#my $t1 = Test::Mojo->new('Payments');
#$t1->get_ok('/services')->status_is(200)->content_like(qr/Mojolicious/i);

#my $t2 = Test::Mojo->new('Payments');
#$t2->get_ok('/checkout')->status_is(200)->content_like(qr/Mojolicious/i);

done_testing();
