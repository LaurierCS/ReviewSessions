import {makeScene2D, Txt} from '@motion-canvas/2d';
import {beginSlide, waitFor, createRef} from '@motion-canvas/core';
import {CodeBlock, lines} from '@motion-canvas/2d/lib/components/CodeBlock';

export default makeScene2D(function* (view) {
  // Create your animations here

  const codeRef = createRef<CodeBlock>();
  
  yield* beginSlide('first slide');
  yield view.add(
    <>
      <CodeBlock
        language='python'
        ref={codeRef}
        fontSize={30}
        alignItems={'center'}

        code={() => `int1 = 10
int2 = -15`}
      /> 
    </>
  );

  yield * codeRef().selection(lines(0), 1);
  yield * waitFor(5);
  yield * codeRef().selection(lines(1), 1);
  yield * waitFor(5);
  });
