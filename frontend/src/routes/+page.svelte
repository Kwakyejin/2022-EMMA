<script>
  import { Heading, P, A, Button } from "flowbite-svelte";

  let c1 = true;
  let c2 = false;
  let c3 = false;
  let c4 = false;

  let visible = false;
</script>

<div class="z-0 bg-cover bg-indigo-200">
  <div class="flex">
    <img src="/PROFILEPIC.svg" class="w-1/6 h-1/3 px-3" alt="Logo" />
    <div>
      <Heading tag="h2" class="mt-5 mb-2">Kwak Yejin</Heading>
      <div class="bg-cover bg-white p-3 rounded-lg">
        <h1>안녕안녕 나는 예진이야~~~</h1>
        <p>헬륨가스 머거떠니 요로케 되찌~~~~</p>
        <p>허리도 아프고 목도 아프고 다 아파아아ㅏ 서러워어어어</p>
        <p>오이시쿠 나레 오이시쿠 나레 모에모에 뀽</p>
      </div>
    </div>
  </div>
  <div class="flex">
    <button
      on:click={() => {
        c1 = true;
        c2 = false;
        c3 = false;
        c4 = false;
      }}
      class="bg-cover {c1
        ? 'bg-point'
        : 'bg-background'} rounded-lg m-3 p-1 w-1/12 flex justify-center"
    >
      <P size="xl" weight="bold" color="text-white">관심직무</P>
    </button>

    <button
      on:click={() => {
        c1 = false;
        c2 = true;
        c3 = false;
        c4 = false;
      }}
      class="bg-cover {c2
        ? 'bg-point'
        : 'bg-background'} rounded-lg m-3 p-1 w-1/12 flex justify-center"
    >
      <P size="xl" weight="bold" color="text-white">자격사항</P>
    </button>

    <button
      on:click={() => {
        c1 = false;
        c3 = true;
        c2 = false;
        c4 = false;
      }}
      class="bg-cover {c3
        ? 'bg-point'
        : 'bg-background'} rounded-lg m-3 p-1 w-1/12 flex justify-center"
    >
      <P size="xl" weight="bold" color="text-white">전공</P>
    </button>

    <button
      on:click={() => {
        c1 = false;
        c4 = true;
        c3 = false;
        c2 = false;
      }}
      class="bg-cover {c4
        ? 'bg-point'
        : 'bg-background'} rounded-lg m-3 p-1 w-2/12 flex justify-center"
    >
      <P size="xl" weight="bold" color="text-white">공모전 및 비교과 활동</P>
    </button>
  </div>

  {#if c1}
    <div class="relative grid grid-cols-3 gap-1">
      <button
        on:click={() => {
          visible = !visible;
        }}
      >
        <div
          class="flex bg-cover bg-white m-1 rounded-lg items-center justify-center"
        >
          <img src="/Rectangle.svg" class="pt-3 w-50 h-50" alt="Logo" />
          <div>
            <P size="xl" weight="bold">삼성 바이오틱스 인턴의 여정</P>
            <p>Visit to read the documentation</p>
          </div>
        </div>
      </button>

      <button
        on:click={() => {
          visible = !visible;
        }}
      >
        <div
          class="flex bg-cover bg-white m-1 rounded-lg items-center justify-center"
        >
          <img src="/Rectangle.svg" class="pt-3 w-50 h-50" alt="Logo" />
          <div>
            <P size="xl" weight="bold">삼성 바이오틱스 인턴의 여정</P>
            <p>Visit to read the documentation</p>
          </div>
        </div>
      </button>

      <button
        on:click={() => {
          visible = !visible;
        }}
      >
        <div
          class="flex bg-cover bg-white m-1 rounded-lg items-center justify-center"
        >
          <img src="/Rectangle.svg" class="pt-3 w-50 h-50" alt="Logo" />
          <div>
            <P size="xl" weight="bold">삼성 바이오틱스 인턴의 여정</P>
            <p>Visit to read the documentation</p>
          </div>
        </div>
      </button>

      <button
        on:click={() => {
          visible = !visible;
        }}
      >
        <div
          class="flex bg-cover bg-white m-1 rounded-lg items-center justify-center"
        >
          <img src="/Rectangle.svg" class="pt-3 w-50 h-50" alt="Logo" />
          <div>
            <P size="xl" weight="bold">삼성 바이오틱스 인턴의 여정</P>
            <p>Visit to read the documentation</p>
          </div>
        </div>
      </button>
    </div>
  {/if}

  {#if c2}
    <div class="relative grid grid-cols-3 gap-1">
      <button
        on:click={() => {
          visible = !visible;
        }}
      >
        <div
          class="flex bg-cover bg-white m-1 rounded-lg items-center justify-center"
        >
          <img src="/Rectangle.svg" class="pt-3 w-50 h-50" alt="Logo" />
          <div>
            <P size="xl" weight="bold">포토샵</P>
            <p>Visit to read the documentation</p>
          </div>
        </div>
      </button>

      <button
        on:click={() => {
          visible = !visible;
        }}
      >
        <div
          class="flex bg-cover bg-white m-1 rounded-lg items-center justify-center"
        >
          <img src="/Rectangle.svg" class="pt-3 w-50 h-50" alt="Logo" />
          <div>
            <P size="xl" weight="bold">기사</P>
            <p>Visit to read the documentation</p>
          </div>
        </div>
      </button>
    </div>
  {/if}

  {#if c3}
    <div class="relative grid grid-cols-3 gap-1">
      <button
        on:click={() => {
          visible = !visible;
        }}
      >
        <div
          class="flex bg-cover bg-white m-1 rounded-lg items-center justify-center"
        >
          <img src="/Rectangle.svg" class="pt-3 w-50 h-50" alt="Logo" />
          <div>
            <P size="xl" weight="bold">의생명융합공학부</P>
            <p>Visit to read the documentation</p>
          </div>
        </div>
      </button>

      <button
        on:click={() => {
          visible = !visible;
        }}
      >
        <div
          class="flex bg-cover bg-white m-1 rounded-lg items-center justify-center"
        >
          <img src="/Rectangle.svg" class="pt-3 w-50 h-50" alt="Logo" />
          <div>
            <P size="xl" weight="bold">정보컴퓨터공학</P>
            <p>Visit to read the documentation</p>
          </div>
        </div>
      </button>
    </div>
  {/if}

  {#if c4}
    <div class="relative grid grid-cols-3 gap-1">
      <button
        on:click={() => {
          visible = !visible;
        }}
      >
        <div
          class="flex bg-cover bg-white m-1 rounded-lg items-center justify-center"
        >
          <img src="/Rectangle.svg" class="pt-3 w-50 h-50" alt="Logo" />
          <div>
            <P size="xl" weight="bold">공모전모전룰루랄라</P>
            <p>Visit to read the documentation</p>
          </div>
        </div>
      </button>

      <button
        on:click={() => {
          visible = !visible;
        }}
      >
        <div
          class="flex bg-cover bg-white m-1 rounded-lg items-center justify-center"
        >
          <img src="/Rectangle.svg" class="pt-3 w-50 h-50" alt="Logo" />
          <div>
            <P size="xl" weight="bold">캬캬캬</P>
            <p>Visit to read the documentation</p>
          </div>
        </div>
      </button>

      <button
        on:click={() => {
          visible = !visible;
        }}
      >
        <div
          class="flex bg-cover bg-white m-1 rounded-lg items-center justify-center"
        >
          <img src="/Rectangle.svg" class="pt-3 w-50 h-50" alt="Logo" />
          <div>
            <P size="xl" weight="bold">ㅎㅎ</P>
            <p>Visit to read the documentation</p>
          </div>
        </div>
      </button>
    </div>
  {/if}

  {#if visible}
    <div
      class="absolute z-40 top-1/6 opacity-95 w-auto h-auto rounded-lg inset-y-0 right-10 m-10 p-5 bg-lightpoint flex flex-col justify-center"
    >
      <img src="/Rectangle.svg" class="pt-3 w-50 h-50" alt="Logo" />
      <p>
        저는 3개월간 인사팀에서 근무했습니다. 인사팀안에도 여러 부서가 있지만,
      </p>
      <p>
        구체적으로는 채용팀에서 근무를 했습니다. 평소 HR직무를 희망했고, HR직무
      </p>
      <p>업무경험이 필요했었습니다. 이 와중에 운좋게도 좋은 직장에서 원하던</p>
      <p>직무에서 일을 해볼 수 있었습니다. 앞서 말씀드린대로, 저는 HR직무를</p>
      <p>
        희망하였기에 일하는 느낌보다는 배운다는 느낌이 강했습니다. 또, 취준생의
      </p>
      <p>
        입장에서 취준생을 상대하는 채용팀에 있으니 기분이 묘하기도 했습니다.
      </p>
      <p>
        각종 채용문의와 면접자들을 상대하면서 취준생의 입장이 아닌 인사담당자의
      </p>
      <p>입장을 생각할수도 있기도했구요. 또, 전반적인 HR프로세스를 익히고</p>
      <p>
        인사팀의 구성원들과 많은 얘기를 하면서 HR직무를 배워갈 수 있었습니다.
      </p>
      <Heading tag="h5" class="font-light"
        >더불어, HR직무에 확신을 가지게 되기도 했습니다.</Heading
      >
    </div>
  {/if}
</div>
