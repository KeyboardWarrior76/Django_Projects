
const comments = [
    {id: 1, name: "Comment 1", parent_id: 2},
    {id: 2, name: "Comment 2", parent_id: 3},
    {id: 3, name: "Comment 3", parent_id: null},
    {id: 4, name: "Comment 4", parent_id: 2},
    {id: 5, name: "Comment 5", parent_id: 3},
    {id: 6, name: "Comment 6", parent_id: null},
]

const printComments = (comments) => {
    const tree = {};
    tree.root = { id: null, children:[] };
    
    /////////QUADRATIC SOLUTION, DON'T DO THIS ///////////
    // comments.push(tree.root);
    // let node;
    //
    // for(let i = 0; i < comments.length; i++){
    //     node = comments[i];
    //
    //     comments.forEach((comment) => {
    //         if(comment.parent_id === node.id) {
    //             if(!node.children) node.children = [];
    //             node.children.push(comment);
    //         }
    //     })
    // }
    ///////////////////////////////////////////////////////


    // LINEAR SOLUTION ---> DO THIS ///////////////////////
    // 1) construct a hash where the keys are ids, and the value is the node
    // 2) loop through the list again, and for each node, find the parentNode in
    //    the hash, and push the currentNode to it's children
    const nodeHash = {};

    comments.forEach((comment) => {
        nodeHash[comment.id] = comment;
    });

    comments.forEach((comment) => {
        if(!comment.parent_id) {
            tree.root.children.push(comment);
        } else {
            let parentNode = nodeHash[comment.parent_id];
            if(!parentNode.children) parentNode.children = [];
            parentNode.children.push(comment);
        }
    });

    const DFS = (node, dashes="") => {
        if(node.name) console.log(dashes, node.name);
        if(node.children) {
            node.children.forEach((child) => {
                DFS(child, !child.parent_id? "" : dashes + "-");
            });
        }
    }

    DFS(tree.root);
}

printComments(comments);

