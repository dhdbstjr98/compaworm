<script>
  export let obj1;
  export let obj2;
  export const getComments = async () => {
    if (!obj1 || !obj2) return;

    try {
      const res = await getCommentsAPI(obj1, obj2);
      comments = res.map(comment => ({
        author: comment.author,
        profile: comment.profile,
        createdAt: comment.created_at,
        comment: comment.comment,
        isLeft: comment.obj == obj1
      }));
    } catch (err) {
      M.toast({ html: "코멘트를 불러오는데 실패하였습니다." });
    }
  };

  import Comment from "~/components/Comment.svelte";
  import { getComments as getCommentsAPI } from "~/api/";

  let comments = [];

  getComments();
</script>

<style>
  .comments {
    margin-top: 2em;
  }
</style>

<div class="comments">
  {#each comments as comment}
    <Comment {...comment} />
  {/each}
</div>
