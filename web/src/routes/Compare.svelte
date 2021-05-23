<script>
  import { push } from "svelte-spa-router";
  import Banner from "~/components/Banner.svelte";
  import Body from "~/components/Body.svelte";
  import Obj from "~/components/Obj.svelte";
  import Comment from "~/components/Comment.svelte";
  import CommentForm from "~/components/CommentForm.svelte";
  import Bar from "~/components/Bar.svelte";

  export let params = {};

  if (!params.obj1 || !params.obj2) push("/");

  // sample
  const comments = [
    {
      name: "윤석",
      profile: null,
      author: 1,
      isLeft: true,
      comment:
        "품었기 인생을 싹이 이상을 예수는 부패뿐이다. 새가 미묘한 인류의 가는 것은 이상은 것이다. 대한 커다란 같은 사막이다. 가치를 끝까지 지혜는 인간의 반짝이는 철환하였는가? 피에 피부가 남는 원대하고, 것은 끝에 작고 이것을 타오르고 있으랴? 튼튼하며, 수 가치를 힘차게 이상을 그들의 가는 노래하며 위하여서 보라.",
      createdAt: "2021.05.24 16:23:11"
    },
    {
      name: "윤석",
      profile: null,
      author: 1,
      isLeft: true,
      comment:
        "청춘에서만 아니더면, 바이며, 부패를 모래뿐일 운다. 실로 생명을 맺어, 꽃이 그림자는 가치를 할지라도 하는 철환하였는가? 방지하는 붙잡아 따뜻한 뛰노는 수 예가 이 그와 것이다. 두손을 우리의 발휘하기 꽃이 없으면, 있을 위하여, 예수는 아름다우냐? 새가 든 그러므로 인생의 소금이라 물방아 사막이다. 그들의 따뜻한 무엇을 구할 그들은 청춘 뛰노는 위하여, 것이다. 청춘 역사를 보내는 공자는 유소년에게서 보이는 남는 착목한는 운다.",
      createdAt: "2021.05.24 16:23:11"
    },
    {
      name: "윤석",
      profile: null,
      author: 1,
      isLeft: false,
      comment:
        "웅대한 남는 피에 오아이스도 열매를 풍부하게 눈에 운다. 뭇 같이, 있으며, 용감하고 꽃 새 가치를 돋고, 살았으며, 것이다. 예수는 길을 있으며, 눈이 작고 얼음 봄바람이다. 싶이 있는 되려니와, 평화스러운 끝까지 얼마나 노래하며 동력은 같은 보라. 역사를 것은 어디 곳으로 청춘의 붙잡아 인간은 이상의 그리하였는가? 거친 예수는 가치를 맺어, 하는 할지라도 쓸쓸하랴? 들어 시들어 인간의 창공에 그들의 오아이스도 두기 것이다.",
      createdAt: "2021.05.24 16:23:11"
    },
    {
      name: "윤석",
      profile: null,
      author: 1,
      isLeft: true,
      comment:
        "인생을 거선의 피에 것이다. 인도하겠다는 뭇 할지라도 쓸쓸한 것이다.보라, 듣는다. 주는 가슴이 뼈 그리하였는가? 피어나는 것이 영락과 교향악이다. 천하를 그림자는 석가는 할지라도 이상 이것이다. 현저하게 사람은 튼튼하며, 있는가?",
      createdAt: "2021.05.24 16:23:11"
    },
    {
      name: "윤석",
      profile: null,
      author: 1,
      isLeft: false,
      comment:
        "풍부하게 얼마나 생명을 봄바람이다. 못할 풀이 따뜻한 운다. 그들은 반짝이는 고행을 갑 얼음에 인생의 주는 위하여서. 이상은 꾸며 이상 끝에 행복스럽고 광야에서 그들은 듣는다. 얼마나 위하여 얼음 트고, 소리다.이것은 불어 몸이 사람은 길지 부패뿐이다.",
      createdAt: "2021.05.24 16:23:11"
    }
  ];
</script>

<style>
  .compare-top {
    background-color: #e0f2f1;
    padding: 20px 0;
  }

  .objs {
    margin-bottom: 2rem;
  }

  .versus {
    text-align: center;
    font-size: 2rem;
    height: 300px;
    line-height: 300px;
    color: #004d40;
  }

  .comments {
    margin-top: 2em;
  }

  @media (max-width: 992px) {
    .versus {
      height: 200px;
      line-height: 200px;
    }
  }

  @media (max-width: 600px) {
    .versus {
      height: 40px;
      line-height: 40px;
      font-size: 1rem;
    }
  }
</style>

<Banner />
<Body>
  <div class="compare-top">
    <div class="container">
      <div class="row objs">
        <div class="col m5 s12">
          <Obj name={params.obj1} />
        </div>
        <div class="col m2 s12 versus">VS</div>
        <div class="col m5 s12">
          <Obj name={params.obj2} />
        </div>
      </div>
      <div class="row">
        <div class="col s12">
          <Bar obj1={params.obj1} obj2={params.obj2} />
        </div>
      </div>
    </div>
  </div>
  <div class="container">
    <CommentForm obj1={params.obj1} obj2={params.obj2} />
    <div class="comments">
      {#each comments as comment}
        <Comment {...comment} />
      {/each}
    </div>
  </div>
</Body>
