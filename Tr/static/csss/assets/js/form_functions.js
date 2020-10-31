function remove_node(id,node_id) {
    if (document.getElementById(id).hasChildNodes()) {
        $(node_id).remove();
    }
}