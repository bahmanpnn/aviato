function SendArticleComment(ArticleId){
    // console.log('SendArticleComment done!!')

    var comment=$('#text').val();
    var parentId=$('#parentId').val();

    $.get('/blog/add-comment/article_comment/',{
        comment:comment,
        article_id:ArticleId,
        parent_id:parentId

    }).then(res=>{
        $('#comments_area').html(res)
        $('#text').val('');
        $('#parentId').val('');
        
        //after adding comment must scroll to that 
        if(parentId !== null && parentId !== ''){
            document.getElementById('single_comment_'+parentId).scrollIntoView({behavior:'smooth'})
        }else{
            document.getElementById('comments_area').scrollIntoView({behavior:'smooth'})
        }
    })
}


function fillParentId(parentId) {
    $('#parentId').val(parentId);
    document.getElementById('comment_form').scrollIntoView({behavior:'smooth'})
}

// product comment
function SendProductComment(productId){
    var comment=$('#text').val();
    var parentId=$('#parentId').val();

    $.get('/products/add-product-comment/comment/',{
        comment: comment,
        product_id: productId,
        parent_id: parentId

    }).then(res=>{
        $('#comments_area').html(res.body)
        $('#text').val('');
        $('#parentId').val('');

        
        //after adding comment must scroll to that 
        if(parentId !== null && parentId !== ''){
            document.getElementById('single_comment_'+parentId).scrollIntoView({behavior:'smooth'})
        }else{
            document.getElementById('comments_area').scrollIntoView({behavior:'smooth'})
        }

    })
}

// end of product comment

function addProductToBasket(productId){
    const count=$('#product-quantity').val();

    $.get('/orders/add-product-to-basket/?product_id=' + productId + '&count='+ count,{
        // count:count,
        // product_id:productId
    }).then(res=>{
        if(res.status=='not-authenticated'){
            Swal.fire({
                title: res.title,
                text:res.text,
                icon: res.icon,
                showCancelButton: true,
                showConfirmButton: true,
                confirmButtonColor: "#3085d6",
                cancelButtonColor: "#d33",
                cancelButtonText:'OK',
                confirmButtonText:res.confirm_button_text,
              }).then((result) => {
                if (result.isConfirmed && res.status === 'not-authenticated') {
                    window.location.href= '/accounts/login/'
                }
              });
        }else{
            Swal.fire({
                title: res.title,
                text:res.text,
                icon: res.icon,
                showConfirmButton: false,
                showCancelButton: true,
                cancelButtonColor: "#d33",
                cancelButtonText:'OK',
            });
        };

    })
}

function addOneToBasket(productId) {
    $.get('/products/add-one-to-basket/?product_id=' + productId,{

    }).then(res=>{
        if(res.status=='not-authenticated'){
            Swal.fire({
                title: res.title,
                text:res.text,
                icon: res.icon,
                showCancelButton: true,
                showConfirmButton: true,
                confirmButtonColor: "#3085d6",
                cancelButtonColor: "#d33",
                cancelButtonText:'OK',
                confirmButtonText:res.confirm_button_text,
              }).then((result) => {
                if (result.isConfirmed && res.status === 'not-authenticated') {
                    window.location.href= '/accounts/login/'
                }
              });
        }else{
            Swal.fire({
                title: res.title,
                text:res.text,
                icon: res.icon,
                showConfirmButton: false,
                showCancelButton: true,
                cancelButtonColor: "#d33",
                cancelButtonText:'OK',
            });
        };

    })
}

function removeOrderDetail(detailId) {
    $.get('/orders/remove_product_from_basket_ajax/?detail_id='+detailId,{
    }).then(res=>{
        if (res.status==='success') {
            $('#basket-content').html(res.body);
        };
    })    
}


function addProductToFavoriteList(productId) {

    $.get('/products/add-to-user-favorite-list/?product_id=' + productId ,{
    }).then(res=>{
        if(res.status=='not-authenticated'){
            Swal.fire({
                title: res.title,
                text:res.text,
                icon: res.icon,
                showCancelButton: true,
                showConfirmButton: true,
                confirmButtonColor: "#3085d6",
                cancelButtonColor: "#d33",
                cancelButtonText:'OK',
                confirmButtonText:res.confirm_button_text,
              }).then((result) => {
                if (result.isConfirmed && res.status === 'not-authenticated') {
                    window.location.href= '/accounts/login/'
                }
              });
        }else{
            const heartIcon=document.getElementById('product_'+res.product_id)
            if(res.action =='removing'){
                heartIcon.classList.remove('favorite-heart');
            }else{
                heartIcon.classList.add('favorite-heart');
            }

            Swal.fire({
                title: res.title,
                text:res.text,
                icon: res.icon,
                showConfirmButton: false,
                showCancelButton: true,
                cancelButtonColor: "#d33",
                cancelButtonText:'OK',
            });
        };

    })
}


// $("#sortingFiltering").change(function testFunc(){
//     $('#sorted-option').onclick(function testFunc(srt) {
//         console.log(srt);
//     })
// })


// $("#sortingFiltering").change(function(){
//     console.log('tested');
//     var sorting=$('#sorted-hidden').val($('#sorted-option').val());
//     console.log(sorting);
// })









// function SendArticleComment(ArticleId){
//     // console.log('SendArticleComment done!!')

//     var comment=$('#commentText').val();
//     var parentId=$('#parentId').val();
//     console.log(comment);
//     console.log(parentId);

//     $.get('/articles/add-comment/article_comment/',{
//         article_comment: comment,
//         article_id: ArticleId,
//         parent_id: parentId

//     }).then(res=>{
//         // res(response is thing that recieve from url and endponin that send data.respone can be httpresponse-render-jsonresponse-filerespone and ...)
//         // console.log(res)

//         $('#comments_area').html(res)
//         $('#commentText').val('');
//         $('#parentId').val('');
        
//         //after adding comment must scroll to that 
//         if(parentId !== null && parentId !== ''){
//             document.getElementById('single_comment_'+parentId).scrollIntoView({behavior:'smooth'})
//         }else{
//             document.getElementById('comments_area').scrollIntoView({behavior:'smooth'})
//         }
//         // location.reload() // this reload the url and page and when use ajax we does not want that! so its useless

//     })
// }

// function fillParentId(parentId) {
//     $('#parentId').val(parentId);
//     document.getElementById('comment_form').scrollIntoView({behavior:'smooth'})
// }

