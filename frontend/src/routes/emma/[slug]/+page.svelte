<script>
  import { Heading, P, A, Button, Span } from "flowbite-svelte";
  import { Spinner } from "flowbite-svelte";
  import { Popover } from "flowbite-svelte";
  import { onMount } from "svelte";
  import { Modal, Label, Input, Textarea } from "flowbite-svelte";
  import {
    Footer,
    FooterLinkGroup,
    FooterLink,
    ImagePlaceholder,
    TextPlaceholder,
    Skeleton,
    FooterCopyright,
  } from "flowbite-svelte";
  let formModal = false;
  import {
    Navbar,
    NavBrand,
    NavLi,
    NavUl,
    NavHamburger,
  } from "flowbite-svelte";
  import { page } from "$app/stores";

  export let data;
  let result;
  let Interest;
  let Qual;
  let Major;
  let Competition;
  let title;
  let story;

  async function get_result() {
    try {
      const response = await fetch(
        `http://10.125.218.100:9025/result?id=${data.id}`,
        {
          mode: "cors",
        }
      );

      if (response.ok) {
        result = await response.json();
        //Interest = result.Interest;
        console.log(result);
      } else {
        console.error("Error:", response.status);
      }
    } catch (error) {
      console.error("Error:", error);
    }
  }

  async function get_Interest() {
    try {
      const response = await fetch(
        `http://10.125.218.100:9025/get_interest?id=${data.id}`,
        {
          mode: "cors",
        }
      );

      if (response.ok) {
        Interest = await response.json();
        console.log(Interest);
      } else {
        console.error("Error:", response.status);
      }
    } catch (error) {
      console.error("Error:", error);
    }
  }

  async function get_Qual() {
    try {
      const response = await fetch(
        `http://10.125.218.100:9025/get_qual?id=${data.id}`,
        {
          mode: "cors",
        }
      );

      if (response.ok) {
        Qual = await response.json();
        console.log(Qual);
      } else {
        console.error("Error:", response.status);
      }
    } catch (error) {
      console.error("Error:", error);
    }
  }

  async function get_Major() {
    try {
      const response = await fetch(
        `http://10.125.218.100:9025/get_major?id=${data.id}`,
        {
          mode: "cors",
        }
      );

      if (response.ok) {
        Major = await response.json();
        console.log(Major);
      } else {
        console.error("Error:", response.status);
      }
    } catch (error) {
      console.error("Error:", error);
    }
  }

  async function get_Competition() {
    try {
      const response = await fetch(
        `http://10.125.218.100:9025/get_competition?id=${data.id}`,
        {
          mode: "cors",
        }
      );

      if (response.ok) {
        Competition = await response.json();
        console.log(Competition);
      } else {
        console.error("Error:", response.status);
      }
    } catch (error) {
      console.error("Error:", error);
    }
  }

  async function fetch_emma() {
    if (c1) {
      try {
        const response = await fetch(
          `http://10.125.218.100:9025/upload_interest?id=${data.id}&input_a=${title}&input_b=${story}`,
          {
            mode: "cors",
          }
        );

        if (response.ok) {
          const result = await response.json();
          console.log(result);
        } else {
          console.error("Error:", response.status);
        }
      } catch (error) {
        console.error("Error:", error);
      }
    } else if (c2) {
      try {
        const response = await fetch(
          `http://10.125.218.100:9025/upload_qual?id=${data.id}&input_a=${title}&input_b=${story}`,
          {
            mode: "cors",
          }
        );

        if (response.ok) {
          const result = await response.json();
          console.log(result);
        } else {
          console.error("Error:", response.status);
        }
      } catch (error) {
        console.error("Error:", error);
      }
    } else if (c3) {
      try {
        const response = await fetch(
          `http://10.125.218.100:9025/upload_major?id=${data.id}&input_a=${title}&input_b=${story}`,
          {
            mode: "cors",
          }
        );

        if (response.ok) {
          const result = await response.json();
          console.log(result);
        } else {
          console.error("Error:", response.status);
        }
      } catch (error) {
        console.error("Error:", error);
      }
    } else {
      try {
        const response = await fetch(
          `http://10.125.218.100:9025/upload_competition?id=${data.id}&input_a=${title}&input_b=${story}`,
          {
            mode: "cors",
          }
        );

        if (response.ok) {
          const result = await response.json();
          console.log(result);
        } else {
          console.error("Error:", response.status);
        }
      } catch (error) {
        console.error("Error:", error);
      }
    }
    location.reload();
  }

  async function delete_emma(d) {
    if (c1) {
      try {
        const response = await fetch(
          `http://10.125.218.100:9025/delete_interest?id=${data.id}&input_a=${d}`,
          {
            mode: "cors",
          }
        );

        if (response.ok) {
          const result = await response.json();
          console.log(result);
        } else {
          console.error("Error:", response.status);
        }
      } catch (error) {
        console.error("Error:", error);
      }
    } else if (c2) {
      try {
        const response = await fetch(
          `http://10.125.218.100:9025/delete_qual?id=${data.id}&input_a=${d}`,
          {
            mode: "cors",
          }
        );

        if (response.ok) {
          const result = await response.json();
          console.log(result);
        } else {
          console.error("Error:", response.status);
        }
      } catch (error) {
        console.error("Error:", error);
      }
    } else if (c3) {
      try {
        const response = await fetch(
          `http://10.125.218.100:9025/delete_major?id=${data.id}&input_a=${d}`,
          {
            mode: "cors",
          }
        );

        if (response.ok) {
          const result = await response.json();
          console.log(result);
        } else {
          console.error("Error:", response.status);
        }
      } catch (error) {
        console.error("Error:", error);
      }
    } else {
      try {
        const response = await fetch(
          `http://10.125.218.100:9025/delete_competition?id=${data.id}&input_a=${d}`,
          {
            mode: "cors",
          }
        );

        if (response.ok) {
          const result = await response.json();
          console.log(result);
        } else {
          console.error("Error:", response.status);
        }
      } catch (error) {
        console.error("Error:", error);
      }
    }
    location.reload();
  }

  let c1 = true;
  let c2 = false;
  let c3 = false;
  let c4 = false;

  onMount(async () => {
    get_result();
    get_Interest();
    get_Qual();
    get_Major();
    get_Competition();
  });
</script>

<Navbar let:hidden let:toggle>
  <NavBrand href="/">
    <img src="/Frame.svg" class="self-center w-4/6 py-3" alt="Logo" />
  </NavBrand>
  <NavHamburger on:click={toggle} />
  <NavUl {hidden}>
    <NavLi
      href="/"
      active={$page.url.pathname === "/" ? true : false}
      class="flex items-center text-xl"
    >
      <img src="/EMMA.svg" class="w-9 h-10 px-3" alt="Logo" />LOGIN</NavLi
    >

    <NavLi
      href="/about"
      active={$page.url.pathname === "/about" ? true : false}
      class="flex items-center  text-xl"
    >
      <img src="/EMMA.svg" class="w-9 h-10 px-3" alt="Logo" />ABOUT</NavLi
    >
  </NavUl>
</Navbar>
{#if result}
  <div class="bg-cover bg-indigo-200 p-10 justify-center">
    <div class="flex">
      <img src="/PROFILEPIC.svg" class="w-1/6 h-1/3 px-3" alt="Logo" />
      <div>
        <Heading tag="h2" class="mt-5 mb-2">{result.name}</Heading>
        <div class="bg-cover bg-white p-3 rounded-lg">
          <h1>{result.intro}</h1>
        </div>
      </div>
    </div>

    <div class="flex justify-between">
      <button
        on:click={() => {
          c1 = true;
          c2 = false;
          c3 = false;
          c4 = false;
        }}
        class="bg-cover {c1
          ? 'bg-point'
          : 'bg-background'} rounded-lg m-3 p-1 w-3/12 flex justify-center"
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
          : 'bg-background'} rounded-lg m-3 p-1 w-3/12 flex justify-center"
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
          : 'bg-background'} rounded-lg m-3 p-1 w-3/12 flex justify-center"
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
          : 'bg-background'} rounded-lg m-3 p-1 w-3/12 flex justify-center"
      >
        <P size="xl" weight="bold" color="text-white">공모전 및 비교과 활동</P>
      </button>
    </div>

    {#if c1}
      {#if Interest}
        <div class="bg-cover bg-white mb-3 p-5">
          <div class="p-3">
            <Heading tag="h2" class="text-center "
              ><Span gradient>관심 직무</Span> 는 개인이 특별히 흥미를 가지고 있거나
              열정을 가지고 추구하는 직무를 말합니다.
            </Heading>
            <P size="xl" weight="medium" class="text-center"
              >이는 개인의 관심, 역량, 가치관 등에 따라 다를 수 있습니다. 관심
              직무는 개인이 일하면서 흥미를 느끼고 즐거움을 느낄 수 있는 분야를
              의미합니다.
            </P>
          </div>
          <P
            >관심 직무를 선택하는 것은 개인의 직업 만족도와 성공을 위해
            중요합니다. 관심 직무를 가진 사람들은 업무에 흥미를 가지고 더 나은
            발전에도 적극적으로 참여할 가능성이 높습니다.
          </P><P
            >관심 직무를 찾기 위해서는 자신의 관심사, 역량, 성향 등을 고려해보는
            것이 중요합니다. 자신이 어떤 분야에 관심이 있는지, 어떤 스킬과
            역량을 보유하고 있는지, 어떤 종류의 일에 대해 열정을 가지고 있는지를
            자문해보는 것이 좋습니다. 이러한 고려를 통해 관심 직무를 찾고 그에
            맞는 진로를 선택할 수 있습니다.</P
          >
        </div>
        <div class="relative grid grid-cols-3 gap-1 bg-cover bg-white p-3">
          <Button class="bg-cover bg-point" on:click={() => (formModal = true)}
            ><P size="2xl" weight="medium" color="white">EMMA 추가하기</P
            ></Button
          >
          {#each Interest as [d, i]}
            <Button id={d} outline color="blue"
              ><P size="2xl" weight="medium" color="white">{d}</P></Button
            >
            <Popover class="w-64 text-sm font-light " title={d} trigger="click">
              <Button
                class="flex place-content-center w-full h-8 p-3"
                on:click={() => delete_emma(d)}
              >
                <img src="/EMMA.svg" class="w-3 h-3 m-1" alt="Logo" />
                <p>데이터 지우기</p></Button
              >

              {i}
            </Popover>
          {/each}
        </div>
      {:else}
        <Spinner />
      {/if}
    {/if}

    {#if c2}
      {#if Qual}
        <div class="bg-cover bg-white mb-3 p-5">
          <div class="p-3">
            <Heading tag="h2" class="text-center "
              ><Span gradient>자격 사항</Span> 은 특정 직무나 업무를 수행하기 위해
              필요한 조건이나 요구사항을 의미합니다.
            </Heading>
            <P size="xl" weight="medium" class="text-center "
              >이는 해당 직무에서 성공적으로 수행하기 위해 필요한 지식, 기술,
              경험 등을 나타냅니다.
            </P>
          </div>
          <P
            >자격 사항은 직무의 성격과 조직의 요구에 따라 다르며, 일반적으로는
            다음과 같은 요소들을 포함할 수 있습니다:
          </P><P
            >학력 요구사항: 일부 직무에서는 특정 학위나 전문 교육을 완료한
            자격이 필요할 수 있습니다. 예를 들어, 공학 직무에서는 공학 학사
            학위가 필요한 경우가 있습니다.</P
          >

          <P
            >전문 기술 및 지식: 특정 분야에서 필요한 기술, 지식, 도구,
            소프트웨어 등에 대한 숙련도가 요구될 수 있습니다. 예를 들어,
            소프트웨어 개발자의 경우 특정 프로그래밍 언어나 개발 도구에 대한
            숙련도가 필요합니다.</P
          >

          <P
            >경력 요구사항: 일부 직무는 특정 경력 수준을 요구할 수 있습니다.
            예를 들어, 고위 관리자 직무는 이전의 관리 경험이 필요할 수 있습니다.</P
          >

          <P>
            인증 및 자격증: 특정 직무에서는 인증이나 자격증을 보유하고 있는 것이
            요구될 수 있습니다. 이는 해당 분야에서의 전문성을 입증하는 데 도움이
            됩니다. 예를 들어, 회계사는 CPA 자격증을 갖추어야 할 수 있습니다.</P
          >
        </div>
        <div class="relative grid grid-cols-3 gap-1 bg-cover bg-white p-3">
          <Button class="bg-cover bg-point" on:click={() => (formModal = true)}
            ><P size="2xl" weight="medium" color="white">EMMA 추가하기</P
            ></Button
          >
          {#each Qual as [d, i]}
            <Button id={d} outline color="blue"
              ><P size="2xl" weight="medium" color="white">{d}</P></Button
            >
            <Popover class="w-64 text-sm font-light " title={d} trigger="click">
              <Button
                class="flex place-content-center w-full h-8 p-3"
                on:click={() => delete_emma(d)}
              >
                <img src="/EMMA.svg" class="w-3 h-3 m-1" alt="Logo" />
                <p>데이터 지우기</p></Button
              >

              {i}
            </Popover>
          {/each}
        </div>
      {:else}
        <Spinner />
      {/if}
    {/if}

    {#if c3}
      {#if Major}
        <div class="bg-cover bg-white mb-3 p-5">
          <div class="p-3">
            <Heading tag="h2" class="text-center "
              ><Span gradient>전공</Span> 은 대학에서 학위 취득을 위해 특정 분야에
              집중적 학습하는 학문적 분야를 말합니다.
            </Heading>
            <P size="xl" weight="medium" class="text-center">
              대학에서는 다양한 학문 분야를 제공하며, 학생들은 자신의 흥미와
              목표에 맞게 원하는 분야를 선택하여 전공을 결정합니다.
            </P>
          </div>
          <P
            >전공은 주로 학위 프로그램을 수행하는 동안 특정 주제에 대해 깊이
            있는 학문적인 지식을 습득하고 이해하는 것을 목표로 합니다. 각 전공은
            해당 분야의 기본 원리, 이론, 방법 및 관련된 실무를 배우는 과정으로
            구성됩니다. 예를 들어, 컴퓨터 과학 전공에서는 프로그래밍, 알고리즘,
            데이터 구조 등에 대한 학습이 포함될 수 있습니다. 또한, 경영학
            전공에서는 경영 이론, 회계, 마케팅, 조직 개발 등과 같은 주제를 다룰
            수 있습니다.
          </P><P
            >전공은 학위를 취득하기 위한 필수 요건이며, 학사 학위, 석사 학위,
            박사 학위 등 다양한 학위 수준에서 전공을 선택할 수 있습니다. 개인의
            관심사와 목표를 고려하여 적절한 전공을 선택하는 것은 학업 및 진로에
            대한 성공적인 결정을 돕는 중요한 단계입니다.</P
          >
        </div>
        <div class="relative grid grid-cols-3 gap-1 bg-cover bg-white p-3">
          <Button class="bg-cover bg-point" on:click={() => (formModal = true)}
            ><P size="2xl" weight="medium" color="white">EMMA 추가하기</P
            ></Button
          >
          {#each Major as [d, i]}
            <Button id={d} outline color="blue"
              ><P size="2xl" weight="medium" color="white">{d}</P></Button
            >
            <Popover class="w-64 text-sm font-light " title={d} trigger="click">
              <Button
                class="flex place-content-center w-full h-8 p-3"
                on:click={() => delete_emma(d)}
              >
                <img src="/EMMA.svg" class="w-3 h-3 m-1" alt="Logo" />
                <p>데이터 지우기</p></Button
              >

              {i}
            </Popover>
          {/each}
        </div>
      {:else}
        <Spinner />
      {/if}
    {/if}

    {#if c4}
      {#if Competition}
        <div class="bg-cover bg-white mb-3 p-5">
          <div class="p-3">
            <Heading tag="h2"
              ><Span gradient>공모전 및 비교과 활동</Span> 은 학교나 기타 조직이나
              기관에서 학사 과정 외에 학생들이 참여하고 기술, 창의성, 리더십 등을
              발전시키는 활동을 말합니다.
            </Heading>
            <P size="xl" weight="medium" class="text-center">
              이러한 활동들은 학생들이 학교 외부에서 실전 경험을 쌓을 수 있으며,
              자기계발과 진로 발전에 도움을 줄 수 있습니다.
            </P>
          </div>
        </div>
        <div class="relative grid grid-cols-3 gap-1 bg-cover bg-white p-3">
          <Button class="bg-cover bg-point" on:click={() => (formModal = true)}
            ><P size="2xl" weight="medium" color="white">EMMA 추가하기</P
            ></Button
          >
          {#each Competition as [d, i]}
            <Button id={d} outline color="blue"
              ><P size="2xl" weight="medium" color="white">{d}</P></Button
            >
            <Popover class="w-64 text-sm font-light " title={d} trigger="click">
              <Button
                class="flex place-content-center w-full h-8 p-3"
                on:click={() => delete_emma(d)}
              >
                <img src="/EMMA.svg" class="w-3 h-3 m-1" alt="Logo" />
                <p>데이터 지우기</p></Button
              >

              {i}
            </Popover>
          {/each}
        </div>
      {:else}
        <Spinner />
      {/if}
    {/if}
  </div>
{/if}

<Modal bind:open={formModal} size="xs" autoclose={false} class="w-full">
  <form class="flex flex-col space-y-6" action="#">
    <Heading class="text-xl font-medium text-gray-900 dark:text-white">
      EMMA 추가하기
    </Heading>
    <Label class="space-y-2">
      <span>EMMA Title</span>
      <Input
        bind:value={title}
        type="text"
        name="Title"
        placeholder="EX) 국내 최고의 미디어 기업, 네이버"
        required
      />
    </Label>
    <Label class="space-y-2">
      <span>EMMA Story</span>
      <Textarea
        id="textarea-id"
        placeholder="EX) 네이버에서의 인턴 일지"
        bind:value={story}
        rows="4"
        name="story"
      />
    </Label>

    <Button class="bg-cover bg-point w-full" on:click={() => fetch_emma()}
      >EMMA 추가하기</Button
    >
  </form>
</Modal>

<Footer class="w-full translate-y-full translate-x-0">
  <FooterCopyright href="/" by="KwakYejin" year={2023} />
</Footer>
