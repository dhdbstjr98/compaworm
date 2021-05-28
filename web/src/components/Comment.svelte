<script>
  export let profile;
  export let comment;
  export let createdAt;
  export let author;
  export let isLeft;
</script>

<style>
  .comment-wrapper {
    margin-bottom: 2em;
  }
  .comment-wrapper:last-child {
    margin-bottom: 0;
  }
  .comment {
    width: fit-content;
    max-width: 80%;
    margin-left: auto;
    border: 1px solid #4db6ac;
    border-radius: 5px;
    padding: 20px;
    padding-left: 90px;
    min-height: 50px;
    position: relative;
  }
  .comment.comment-left {
    margin-left: 0;
  }
  .comment .profile {
    position: absolute;
    top: 20px;
    left: 20px;
    width: 50px;
    height: 50px;
    border: 1px solid #4db6ac;
    border-radius: 50%;
    overflow: hidden;
  }
  .comment .content {
    min-height: 50px;
  }
  .comment .text .name {
    font-weight: 600;
    font-size: 0.9em;
    margin-bottom: 0.5em;
  }
  .comment .text p {
    margin: 0;
    margin-bottom: 0.5em;
    font-size: 0.9em;
    white-space: pre-line;
  }
  .comment .date {
    font-size: 0.8em;
    text-align: right;
    color: #80cbc4;
  }
  .profile img {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
</style>

<div class="comment-wrapper">
  <div class="comment" class:comment-left={isLeft}>
    <div class="profile">
      <img
        src={profile ? profile : './img/profile_no_image.png'}
        alt={author} />
    </div>
    <div class="content">
      <div class="text">
        <div class="name">{author}</div>
        <p>{comment}</p>
      </div>
      <div class="date">{createdAt}</div>
    </div>
  </div>
</div>
