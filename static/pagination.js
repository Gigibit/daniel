// basic paging logic to demo the buttons
var pr = document.querySelector( '.paginate.left' );
var pl = document.querySelector( '.paginate.right' );

pr.onclick = slide.bind( this, -1, false );
pl.onclick = slide.bind( this, 1, false );
const urlParams = new URLSearchParams(window.location.search);
const page = Number(urlParams.get('page') ?? '1');

var index = page - 1, total = document.querySelectorAll('.pagination-control a').length;

function slide(offset, initializating) {

  document.querySelector( '.counter' ).innerHTML = page + ' / ' + total;

  pr.setAttribute( 'data-state', page === 1 ? 'disabled' : '' );
  pl.setAttribute( 'data-state', page === total ? 'disabled' : '' );
  if ( initializating || page + offset === 0 || page + offset > total) return
  location.href = location.href.indexOf('page=') != -1 ? 
                    location.href.replace(/(page=)(\d+)(.*)/gi, '$1' + (page + offset) + '$3' ) :
                       location.href + '?page=' + ( page + offset )

}

slide(page-1, true);